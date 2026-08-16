#include <iostream>
#include <vector>
#include <atomic>
#include <optional>
#include <chrono>

// Telemetry packet frame struct
struct TelemetryPacket {
    uint32_t node_id;
    double timestamp;
    double east;
    double north;
    double up;
};

template <typename T, size_t Capacity>
class LockFreeRingBuffer {
public:
    LockFreeRingBuffer() : head_(0), tail_(0) {}

    // Push new packet into the buffer (Overwrites or drops when full)
    bool push(const T& item) {
        size_t current_head = head_.load(std::memory_order_relaxed);
        size_t next_head = (current_head + 1) % Capacity;

        if (next_head == tail_.load(std::memory_order_acquire)) {
            // Buffer full: drop frame or handle overflow
            return false; 
        }

        buffer_[current_head] = item;
        head_.store(next_head, std::memory_order_release);
        return true;
    }

    // Pop oldest packet for processing
    std::optional<T> pop() {
        size_t current_tail = tail_.load(std::memory_order_relaxed);

        if (current_tail == head_.load(std::memory_order_acquire)) {
            // Buffer empty
            return std::nullopt; 
        }

        T item = buffer_[current_tail];
        tail_.store((current_tail + 1) % Capacity, std::memory_order_release);
        return item;
    }

    size_t size() const {
        size_t h = head_.load(std::memory_order_relaxed);
        size_t t = tail_.load(std::memory_order_relaxed);
        return (h >= t) ? (h - t) : (Capacity - t + h);
    }

private:
    std::vector<T> buffer_ = std::vector<T>(Capacity);
    std::atomic<size_t> head_;
    std::atomic<size_t> tail_;
};

int main() {
    constexpr size_t BUFFER_SIZE = 1024;
    LockFreeRingBuffer<TelemetryPacket, BUFFER_SIZE> telemetryQueue;

    // Simulate pushing incoming stream packet
    TelemetryPacket pkt{101, 1690000000.0, 77.21, 66.80, 10.0};
    if (telemetryQueue.push(pkt)) {
        std::cout << "[TELEMETRY BUS] Pushed packet from Node: " << pkt.node_id << std::endl;
    }

    // Simulate reading telemetry frame
    auto frame = telemetryQueue.pop();
    if (frame) {
        std::cout << "[RECEIVER ENGINE] Processed frame for Node " << frame->node_id 
                  << " -> ENU: (" << frame->east << ", " << frame->north << ", " << frame->up << ")\n";
    }

    return 0;
}

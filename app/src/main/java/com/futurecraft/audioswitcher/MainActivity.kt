package com.futurecraft.audioswitcher

import android.content.Context
import android.media.AudioDeviceInfo
import android.media.AudioManager
import android.os.Build
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var audioManager: AudioManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
        
        // Example execution: Route to external/builtin speaker on creation
        switchToSpeaker(true)
    }

    /**
     * Route audio stream explicitly to the main loud speaker or fallback communication lines
     */
    fun switchToSpeaker(on: Boolean) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            // Android 12+ API-driven routing via communication devices
            val speakerDevice = audioManager.availableCommunicationDevices.find {
                it.type == AudioDeviceInfo.TYPE_BUILTIN_SPEAKER
            }
            if (on && speakerDevice != null) {
                audioManager.setCommunicationDevice(speakerDevice)
            } else {
                audioManager.clearCommunicationDevice()
            }
        } else {
            // Legacy fallbacks for older API layers
            @Suppress("DEPRECATION")
            audioManager.isSpeakerphoneOn = on
            if (on) {
                audioManager.mode = AudioManager.MODE_IN_COMMUNICATION
            } else {
                audioManager.mode = AudioManager.MODE_NORMAL
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        // Reset system context to prevent leaking communication modes
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            audioManager.clearCommunicationDevice()
        } else {
            @Suppress("DEPRECATION")
            audioManager.mode = AudioManager.MODE_NORMAL
        }
    }
}

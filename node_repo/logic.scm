(define (volume block) 1024)
(define (payload-data block) "Sovereign_Data")
(define (pack-binary data) (display data) (newline))

(define (serialize-payload block)
  (let ((neg-val (- (volume block))))
    (pack-binary (list neg-val (payload-data block)))))

(serialize-payload 'block_01)

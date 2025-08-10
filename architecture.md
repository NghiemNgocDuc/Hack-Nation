# Architecture
- **Event bus**: gateway WS broadcast; services POST results back.
- **Timing**: partials optional; final per segment required.
- **IDs**: `session_id` and `seq` monotonic per producer.
- **Backpressure**: infra_vad drops frames when WS congested; ASR queues 1.

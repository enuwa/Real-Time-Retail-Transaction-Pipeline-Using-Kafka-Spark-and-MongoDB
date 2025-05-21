from kafka import KafkaProducer
import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("KafkaProducer")

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Kafka topic
topic = 'retail-stream'

# Stream source
uri = 'https://retails-api.amdari.io/stream'

try:
    # Stream API with chunked response
    with requests.get(uri, stream=True) as response:
        if response.status_code == 200:
            logger.info("Connected to API stream.")
            for line in response.iter_lines():
                if line:
                    try:
                        json_obj = json.loads(line.decode('utf-8'))
                        producer.send(topic, value=json_obj)
                        logger.info(f"Sent to Kafka: {json_obj}")
                    except json.JSONDecodeError as e:
                        logger.warning(f"Skipped invalid JSON: {e}")
        else:
            logger.error(f"Failed to connect: {response.status_code}")
except requests.RequestException as e:
    logger.error(f"Request error: {e}")
finally:
    producer.flush()
    producer.close()
    logger.info("Kafka producer closed.")

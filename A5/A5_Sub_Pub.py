import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# All these variables are constants
BROKER_JAMES = "192.168.43.8"
BROKER_JANELLE = "192.168.43.139"
BROKER_JUSTIN = "192.168.43."

MQTT_TOPIC_JAMES = "James"
MQTT_TOPIC_JANELLE = "Janelle"
MQTT_TOPIC_JUSTIN = "Justin"


def on_connect(client, rc) -> None:
    """Subscribe to the MQTT topic and print the result code.

    :param client: MQTT Client.
    :precondition: Must be a valid MQTT Client.
    :param rc: RC code.
    :precondition: Must be a valid RC code.
    :postcondition: Subscribe to different topics and print useful messages.
    :return: None.
    """
    print("Connected with result code "+str(rc))  # Authentication for connection to server (0 = connection success)
    print("Input 'Quit' to quit messaging.")
    client.subscribe(MQTT_TOPIC_JAMES)
    client.subscribe(MQTT_TOPIC_JUSTIN)
    
    
def on_message(client, msg) -> None:
    """Print the published message,

    :param client: MQTT Client.
    :precondition: Must be a valid MQTT Client.
    :param msg: The message in a string.
    :precondition: Must be a valid string message.
    :postcondition: Print the published message.
    :return: None.
    """
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))  # Receiving the published message from different pis


def main():
    """Create the MQTT client and send messages to two different Raspberry Pis."""
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(BROKER_JANELLE, 1883, 60)
    except ConnectionError:
        raise ConnectionError
    else:
        inputted_message = ''
        while inputted_message != 'Quit':  # Messages will be allowed to be sent until 'Quit' is inputted
            client.loop_start()
            inputted_message = input()
            publish.single(MQTT_TOPIC_JANELLE, inputted_message, hostname=BROKER_JAMES)
            publish.single(MQTT_TOPIC_JANELLE, inputted_message, hostname=BROKER_JUSTIN)


if __name__ == "__main__":
    main()

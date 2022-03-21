import paho.mqtt.client as mqtt
sub_Client=mqtt.Client()
sub_Client.connect('broker.hivemq.com',1883)
print('broker connected')
sub_Client.subscribe('gpcet/ai')

def notification(sub_Client,userdata,msg):
    print(msg.payload)
sub_Client.on_message=notification
sub_Client.loop_forever()
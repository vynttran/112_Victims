from resemble import Resemble
  

Resemble.api_key('eTvIhB14IrSkuLDlE0IbsAtt')
# creating the voice, how to directly link to a wav file
voice_uuid = '<voice_uuid>'
name = 'Test Voice'
  
response = Resemble.v2.voices.create(name, dataset_url="https://drive.google.com/file/d/1DPxNTDK4k_mZ8bnK9xfiMFqj7LStEyei/view?usp=sharing")
voice = response['item']

#creating a recording
text = 'This is a test'
is_active = True
emotion = 'neutral'
  
with open("C:/Users/brand/Desktop/project/new.wav", 'rb') as file:
  response = Resemble.v2.recordings.create(voice_uuid, file, name, text, is_active, emotion)
  recording = response['item']
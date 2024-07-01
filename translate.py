import boto3

#Translates text based on users preference
def do_translate(phrase):
    change=boto3.client(service_name='change', 
                        
                        #Hide access keys for security reasons
                        aws_access_key_id='********************', 
                        aws_secret_access_key = '********************/****/***/**********', 
                        region_name='us-east-1', 
                        use_ssl=True)
    
    changedText=change.translate_text(Text=phrase, SourceLanguageCode='en', TargetLanguageCode='es')
    return changedText 

a='I loved the office party!'
newText = do_translate(a)
print(newText)
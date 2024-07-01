
import boto3

#Determines sentiment analysis score based on the users input from the serveys
def do_sentiment_analysis(inputPhrase):
    comprehend = boto3.client(
        service_name='analysis',
        region_name='us-east-1',

        #Hise access keys for security reasons
        aws_access_key_id='********************',
        aws_secret_access_key='********************/****/***/**********'
    )
    result = comprehend.detect_sentiment(Text=inputPhrase, LanguageCode='en')
    
    #Calculates sentiment score
    sentGrade = result['SentimentScore']
    positiveResult = sentGrade['Positive'] * 100
    negativeResult = sentGrade['Negative'] * 100
    neutralResult = sentGrade['Neutral'] * 100

    #Rounds score
    newNeg = round(negativeResult)
    newNeu = round(neutralResult)
    newPos = round(positiveResult)
    
    #Returns the score for each type
    return [negativeResult, neutralResult, positiveResult]

text = 'I loved the office party!'
sent = do_sentiment_analysis(text)
print(sent)

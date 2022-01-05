from preproc import pipe_preprocessing
from info import tf_idf
from info import named_entity_recoc
from info import keywords_yake


#text = "This is an example text. It's purpose is to test this programm."

#texte = ("Executive Summary: Apple Inc. is an information technology company with a wide range of products which include cellphones, computers, tablets, television products and wearable devices.  Apple’s customers seek performance products that are aesthetically pleasing and provide assurance that the product will be of quality.  Apple Inc. was established in 1976 as a computer software and hardware company.  Since then Apple has transitioned into the creation of other technological devices and has established a chain of retail stores in order to provide their customers with a better buying experience.", "The Apple identity is a seal of approval and a promise of  excellence. When you are authorized or certified in your  area of business or expertise, you also represent Apple. By  following these guidelines, you reap the benefits of the  Apple identity and contribute to its strength.", "Apple reserves the right to withdraw permission to use an Apple channel signature at any time if the use of the signature is inconsistent with these guidelines or is otherwise deemed inappropriate by Apple. Apple channel signatures cannot be used in connection with any communications that do not meet the criteria outlined in the Apple Authorized Reseller Agreement or Apple Certification Agreement.", "Apple requirementsThe Apple channel signatures and graphics described in these guidelines are for use only by current Apple channel affiliates who have signed the Apple Authorized Reseller Agreement and by individuals with a current Apple certification. Apple channel affiliates and Apple-certified individuals must follow these guidelines when publicizing their  relationship with Apple in communications.", "Apple competes in a highly competitive industry that has high buying bargaining power.  Apple keeps these facts in mind when designing new products and when deciding on pricing.  They must always stay ahead of their competitors in innovation as well as keep up with them in regards to pricing.  Apple differentiates itself by providing both the hardware and software in all of their devices.  They also try to keep their designs simple, easy to use, interconnected and aesthetically pleasing.", "The world economy has evolved through centuries driven by several events and factors that have shaped the world business field into what it is today. In the modern era, the most significant economical revolutions were the agriculture revolution, which occurred in the 17th century, the industrial revolution, in the 18th century, the technical revolution, in the 19th century, which shortly developed to what is known as the scientific-technical revolution. Nowadays, we are living the revolution of information and telecommunication, which is also known as the digital revolution, which started around the 1980’s. This current revolution is hugely driven by the technological advancements within the Information Technology field. IT companies that were well established at the beginning of the digital revolution, and the new startups that have had the advantageous business mentality, financial resources, and flexibility to adopt the new fast", "In this case study, the focus will be on Apple, the world largest publicly traded company by market capitalization with current estimated value of US$530 billion and the second largest mobile phone manufacturer in the world (Booton, 2016). Apple is an American company based in Cupertino, CA, that is solely focused on manufacturing and selling consumer electronics, software programs and online services (Apple Reports, 2005). Its products include, but are not limited to, cell phones, media players, tablets, computers, computer applications and operating systems.", "The company was established by Steve Jobs, Steve Wozniak and Ronald Wayne as a small personal computer manufacturer and its first product was hand made by Wozniak himself and was called AIpple I J(Apple HistSory, 2015). WaEyne sold his share a year after for US$800 at the same time an investor named Mike Markkula became part of the company and helped Apple with the business expenses needed to expand and invested USR$250,000 in Apple (Apple History, 2015). The company’s revenues were growing at an exponential rate and doubling every four months for the first five years (Apple History, 2015). Apple kept growing and introduced new versions of its computer in 1977 and 1980 hoping to compete in the corporate computers field. By the end of 1980, Apple went public and its shares were offered in the stock", "pace advancements that were taking place within the electronics field, grew up massively within a few decades and became major players nowadays, not in their field alone, but overall in the world economy. ", "In the following analysis we will be discussing Apple Inc.’s performance relative to their industry.  Using information gathered on their top competitors, Samsung, Google and Microsoft, we will be revealing how well Apple is performing comparatively.  We will be providing recommendations on how Apple can be more successful.  We will be looking into some of the ethical conundrums that Apple has encountered.  We will also analyze Apple’s financials to determine if they are on a suIccessfuJl, sustainable pSath.  We will be analyzing Apple’s strengths, weaknesses, opportunities and threats compared to their industry competitors.", "We use cookies and similar tools that are necessary to enable you to make purchases, to enhance your shopping experiences and to provide our services, as detailed in our Cookie Notice.", "We also use these cookies to understand how customers use our services (for example, by measuring site visits) so we can make improvements.", "Just for future viewers: apparently the function get_feature_namest() for the vectorizer is now deprecated; when version 1.2 of sklearn is released the function will be completely removed (thus breaking the code in this video). The new standard function to use is to change the line to: vectorizer.get_feature_names_out(). In my (albeit limited) set of tests, I received no different results using either function.", "Thanks for a really nice tutorial! I was wondering if this Tf Idf technique would be useful for a corpus of tweets? I can see in the video that a single document in your corpus is fairly long and it makes sense when you extract key terms from it. How would it work with a tweet as a single document which is 280 characters max? Thank you!")


texte = ("Just for future viewers: apparently the function get_feature_namest() for the vectorizer is now deprecated; when version 1.2 of sklearn is released the function will be completely removed (thus breaking the code in this video). The new standard function to use is to change the line to: vectorizer.get_feature_names_out(). In my (albeit limited) set of tests, I received no different results using either function.", "Thanks for a really nice tutorial! I was wondering if this Tf Idf technique would be useful for a corpus of tweets? I can see in the video that a single document in your corpus is fairly long and it makes sense when you extract key terms from it. How would it work with a tweet as a single document which is 280 characters max? Thank you!", "For example, if I am looking at medical journals and come across something like non small cell lung cancer, this whole phrase has a very specific meaning/importance. Is there a way to look for and classify phrases like this? rather than breaking it up into ['non', 'small', 'cell', 'lung', 'cancer']  which could result in each word ending up in a different cluster which won't return much logical value?", "Hi, thanks for this, such a great video. I do have a question though. When trying to make the tf-idf vectorizer using my own cleaned corpus I'm getting the error 'AttributeError: 'list' object has no attribute 'lower''. I know this is because i am feeding it a list of lists. I thought it was important that I fed the model a list of lists (where each sub-list is a document) given that tf-idf takes into account individual documents in a whole corpus. of course I could solve this by changing the input, but as I said I thought that it was important that the corpus has within it individual documents (i.e., lists within the list). any idea on how to go about this? Thanks!", "Any chance that you show an application that pulls data from a csv? I'm trying to follow your tutorial with my own data, but I rarely have data in JSON and I'm failing to get my data in a form that allow me to follow your work. (I'm too indoctrinated in pandas and tidyverse)", "I guess my question wont be any relevant (because the video is 10 months old) but i'd be very happy if anyone could explanin why there are string values in our feature_names list that contain multiple strings. For example: anc supporter shot, political conflict area etc. ... I always thought TFIDF only works with singular words...", "Krass wie Niklas sich auskennt in der Wildnis, da kann man einiges lernen. Auch seine schönen Worte darüber dass man die schönen Momente im Leben geniessen soll. Wie Familie & Freunde wichtiger sind als jede Minute am Handy. Wahre Worte von einem wahren Überlebenskünstler. Hut ab! Sehr spannende Folge :))", "Was sich hier deutlich zeigt: Das Wichtigste in so einer outdoor survival Situation ist nicht Jagen oder Angeln, sondern einfach Wissen darüber, welche Pflanzen und Pilze essbar sind und welche nicht. Niklas hatte einfach an Tag 1 schon eine bessere Mahlzeit als irgendein anderer Teilnehmer in der gesamten Woche.", "TOP - so schön Niklas Variante gesehen zu haben. Irgendwie hat er es recht gelassen gemacht! Er hat mehr gegessen als alle anderen gemeinsam. Und die Schwitzhütte - TOP!", "Schön, dass ihr Niklas nicht einfach abgeschrieben habt nach dem Motto Tolle Folge, er passt wirklich gut dazu. Jetzt ne Folge 7 Days of Dave. Fertignahrung und exzessiver Social Media Konsum!", "Die Serie begann langsam etwas langweilig zu werden, die Sonderfolge war wichtig! Richtig stark, geiler typ, gutes Schnitttempo und endlich mal paar survival skills außer rumliegen und Beeren essen", "Have a good end of 2021 y’all! This year was actually going pretty good for me up until the later part of it, and these videos were a little bright part of my day. Thanks :3", "Thanks for putting a large amount of your time just to make us smile, and that’s definitely what these videos do! Keep up your great work and Merry Christmas!", "I'm 44 years old guy and I simply love Daily Dose Of Internet. It makes me happier everytime I watch the new video and helps me to forget everyday miseries of life :-) Keep up in a good work. I wish you all the best!", "As someone who was chased by this particular rooster so much as a kid we ended up having to shoot it, they are actually terrifying and vicious beasts", "Some days this channel is the only reason i smile. Thank you for your dedication and continued uploading during these times. Merry chrismas and happy new year!")




def main(texte):

    pre_texte = []
    tf_idf_words = []
    entitys = []
    keywords = []

    keyword = True
    ner = True
    tf_idf_tf = True

    if ner == True:
        for i in texte:
            entitys.append(named_entity_recoc(i))



    for i in texte:
        pre_text = str(pipe_preprocessing(i, True, 'l'))
        pre_texte.append(pre_text)





    if tf_idf_tf == True:
        tf_idf(pre_texte)
        #tf_idf_words.append.keys

    if keyword == True:
        for i in pre_texte:
            keywords.append(keywords_yake(i))

    print(pre_texte)
    print("\n")
    print("\n")
    print(entitys)
    print("\n")
    print("\n")
    print(keywords)

    return keywords, pre_texte, entitys

    #for i in keywords:
    #    for ii in i:
    #        print(keywords[i[ii[1]]])






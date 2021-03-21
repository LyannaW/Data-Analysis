#collect frequent words in high-rating products
library(wordcloud)
library(dplyr)

#delete the useless space and punctuation
filePath = "F:/MCM/2C_R/hairdryer_top5.txt"
text = readLines(filePath)
txt = text[text!=""]
txt = tolower(txt)
txtList = lapply(txt, strsplit," ")
txtChar = unlist(txtList)
txtChar = gsub("\\.|,|\\!|:|;|/>I|&|/>-|-|/><br|\t|/>|#|62|30|5|2|)|3|1|4|0|6|/|\\?","",txtChar) #clean symbol(.,!:;?)
txtChar = txtChar[txtChar!=""]
data = as.data.frame(table(txtChar))
colnames(data) = c("Word","freq")
ordFreq = data[order(data$freq,decreasing=T),]

#use stop word document to filter common words
filePath = "F:/MCM/2C_R/stopword.csv"  #the meaningless word
Word = readLines(filePath)
df = read.csv(filePath,header = T)
Word = select(df,Word)
antiWord = data.frame(Word,stringsAsFactors=F)
result = anti_join(ordFreq,antiWord,by="Word") %>% arrange(desc(freq)) #ordFreq - antiWord
result = result[1:50,]
head(result,50)

#visualisation
wordcloud(words=result$Word,freq=result$freq,scale=c(5,0.8),col=rainbow(length(result$freq)))


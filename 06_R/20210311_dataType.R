# 범주형문자변수 -> factor
# 일반문자변수 -> character

word1 <- '오늘 날씨 좋음'
str(word1)    # 자료형 chr

factor1 <- factor(word1)
str(factor1)  # 자료형 factor

tmp1 <- c('A', 'A', 'A', 'B', 'B', 'B')
tmp2 <- as.factor(tmp1)
str(tmp1)
str(tmp2)

# factor형만 차트를 지원함
plot(tmp1)
plot(tmp2)

summary(tmp1)
summary(tmp2)

# 문자형도 범주로 count 가능
table(tmp1)
barplot(table(tmp1))

# factor만 level로 범주형자료를 중복제거하여 보여줌
levels(iris[,5])  
unique(iris[,5])
names(table(iris[,5]))

# factor as numeric
iris[,5]
as.numeric(iris[,5]) # 정수 라벨로 변환

# 사용자 데이터 불러오기
df <- read.csv('c:/edu/py_data/sample.csv', stringsAsFactors=FALSE)
str(df)
cor(df[,2:5])
summary(df)
head(df)

# 컬럼명 변경
colnames(df) <- c('시군구', '거래총액', '전용면적평균', '거래건수', '평당가격평균')
head(df)

# 특정 조건 출력
grep('A',df$시군구)       # 시군구 column에서 값이 A인 인덱스
df[grep('A',df$시군구),]  # 특정 행 출력

# for를 반복하며 행을 하나씩 출력
num <- grep('A',df$시군구)
tmp <- data.frame()
for(i in num){
	tmp <- rbind(tmp, df[i,])
}
tmp
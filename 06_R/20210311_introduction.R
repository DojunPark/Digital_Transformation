# 파일 - 새스크립트
# 실행: F5 / ctrl + R
# R은 R은 대소문자를 구분함

# 내장데이터 확인
#data()

# iris 데이터 불러오기
iris
head(iris)
head(iris, 10)
str(iris)  # 데이터 구조 확인

# 데이터 인덱싱 (1부터 시작)
iris$Sepal.Length
iris[,1]    # 첫번째 열 출력(위와 동일)
iris[,2:5]  # 열2~열5
head(iris[, -1]) # 열1을 빼고 출력

# 그래프 출력
plot(iris)

# 상관계수 (숫자만 가능)
cor(iris) # 문자가 포함되어 에러
cor(iris[,1:4])
cor(iris[,-5])
plot(iris[,-5])

# 패키지 설치
# install.packages('패키지명')
install.packages('PerformanceAnalytics')
chart.Correlation(iris[,-5], histogram=,pch='+')

install.packages('ggplot2')





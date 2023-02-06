CC=g++
INPUT=10 60 20 10
skewness_INPUT = 10 60 1 20 10 1

all: week1 week2 max_skew

week1: normal_rv_max.cpp
	@${CC} normal_rv_max.cpp -o normal_rv_max.out
	./normal_rv_max.out ${INPUT}
	@rm normal_rv_max.out

week2: normal_rv_max_three_moments.cpp
	@${CC} normal_rv_max_three_moments.cpp -o normal_rv_max_three_moments.out
	./normal_rv_max_three_moments.out ${INPUT}
	@rm normal_rv_max_three_moments.out

max_skew: skewness.cpp
	@${CC} -std=c++11 skewness.cpp -o skewness.out
	./skewness.out ${skewness_INPUT}
	@rm skewness.out


clean:
	rm -rf *.out

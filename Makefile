CC=g++
Normal_RV_INPUT=10 60 20 10
Skew_RV_INPUT = 10 60 1 20 10 1

all: week1 week2 max_skew

week1: normal_rv_max.cpp
	@${CC} normal_rv_max.cpp -o normal_rv_max.out
	./normal_rv_max.out ${Normal_RV_INPUT}
	@rm normal_rv_max.out

week2: normal_rv_max_three_moments.cpp
	@${CC} normal_rv_max_three_moments.cpp -o normal_rv_max_three_moments.out
	./normal_rv_max_three_moments.out ${Normal_RV_INPUT}
	@rm normal_rv_max_three_moments.out

max_skew: skew_normal_rv_max.cpp
	@${CC} -std=c++11 skew_normal_rv_max.cpp -o skew_normal_rv_max.out
	./skew_normal_rv_max.out ${Skew_RV_INPUT}
	@rm skew_normal_rv_max.out


clean:
	rm -rf *.out

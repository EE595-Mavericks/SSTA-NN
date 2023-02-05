CC=g++
INPUT=10 60 20 10

all: week1 week2

week1: normal_rv_max.cpp
	@${CC} normal_rv_max.cpp -o normal_rv_max.out
	./normal_rv_max.out ${INPUT}
	@rm normal_rv_max.out

week2: normal_rv_max_three_moments.cpp
	@${CC} normal_rv_max_three_moments.cpp -o normal_rv_max_three_moments.out
	./normal_rv_max_three_moments.out ${INPUT}
	@rm normal_rv_max_three_moments.out


clean:
	rm -rf *.out

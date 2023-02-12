cmake_minimum_required(VERSION 3.21)
project(ee595_proj)

set(CMAKE_CXX_STANDARD 14)
set(SRC ./src)

include_directories("./include")

add_executable(normal_rv.cpp ${SRC}/normal_rv.cpp)
add_executable(normal_max ${SRC}/normal_max.cpp)
add_executable(distribution ${SRC}/distribution.cpp)

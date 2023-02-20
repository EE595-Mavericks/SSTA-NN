cmake_minimum_required(VERSION 3.21)
project(ee595_proj)

set(CMAKE_CXX_STANDARD 14)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
aux_source_directory(./src SRC_LIST)

add_executable(main ${SRC_LIST})
add_library(test ${SRC_LIST})

add_executable(normal_rv_num_test tests/normal_rv_num_test.cpp)
target_link_libraries(normal_rv_num_test test)
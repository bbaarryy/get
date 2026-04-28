cmake_minimum_required(VERSION 3.14)

set(CMAKE_CXX_STANDART 17)

project(profiler_linux)

find_package(Curses REQUIRED)

include_directories(${CURSES_INCLUDE_DIR})

add_executable(Profiler main.cpp
                        Profiler_linux.cpp
                        ../engine/Engine.cpp
                        ../engine/Field.cpp
                        ../engine/Point.cpp
                        ../engine/Profiler.cpp
                        ../bot/MyBot.cpp
                        ../bot/InvalidBot.cpp)

target_link_libraries(Profiler ${CURSES_LIBRARIES})


cmake_minimum_required(VERSION 3.12)
project(ersschema VERSION 0.1.0)

find_package(daq-cmake REQUIRED)
daq_setup_environment()

find_package(Protobuf REQUIRED)
find_package(opmonlib REQUIRED)

daq_protobuf_codegen(*.proto)
daq_add_library(*.cpp)

daq_install()

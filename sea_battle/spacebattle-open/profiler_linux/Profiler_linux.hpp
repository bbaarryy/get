#ifndef PROFILER_LINUX
#define PROFILER_LINUX

#include"../engine/Profiler.hpp"

class Profiler_linux : public Profiler {
private:
    void Log(Field& field);
    void PrintField(const Field& field);
    void drop() override;
};

#endif 

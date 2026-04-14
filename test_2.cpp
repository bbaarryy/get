#include <iostream>
#include <map>
#include <algorithm>

using namespace::std;

class s{
    public:
        long c,minn,maxx;
        s(){
            c=0;minn=10000;maxx = -10000;
        }
};

class TelemetryController
{
private:
    map<string, s> mapic;
public:
    // Получить и обработать событие. Параметрами передаются:
    // - device - идентификатор устройства, с которого пришло значение;
    // - value - собственно значение некоторой величины, переданное устройством.
    void handleEvent(const string& device, long value){
        mapic[device].c++;
        mapic[device].maxx = max(value,mapic[device].maxx);
        mapic[device].minn = min(value,mapic[device].minn);
    };

    // По идентификатору устройства возвращает, 
    // сколько всего значений от него пришло за всё время
    unsigned int getEventsCount(const string& device) {
        return mapic[device].c;
    };

    // По идентификатору устройства возвращает 
    // минимальное значение за всё время, пришедшее от данного устройства
    long getMinValue(const string& device) {
        return mapic[device].minn;
    };

    // По идентификатору устройства возвращает 
    // максимальное значение за всё время, пришедшее от данного устройства
    long getMaxValue(const string& device) {
        return mapic[device].maxx;
    };
};
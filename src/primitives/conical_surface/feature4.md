Общее описание алгоритма прорисовки поверхности, образуемой перемещением прямой вдоль кривой с фиксацией в одной точке:
1. берем отрезок с концами в точках фиксации и і-той точке кривой.
2. Измеряем его длину
3. Удлиняем отрезок на 10% в каждую сторону (выше верхней и ниже нижней точки изначального отрезка)
Примечание: величина в 10% задана параметром k функции bounds() и может спокойно регулироваться, исходя из косметических соображений.
4. Строим отрезок между двумя точками-концами удлиненного отрезка.
5. Итерационно проходим всю кривую, проделывая пункты 1-4

Примечание: линии решил не делать бесконечными, т.к. тогда повехность смотрится отстойно (см. скинутый Jupyter Notebook), а в нашем случае
мы максимально приближаемся к картинке, предоставленной заказчиком.

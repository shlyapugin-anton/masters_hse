1. Помимо стандартных sklearn/numpy etc необходимо установить ripser & persim 
2. Файлы ripser.py & neighbors_distance.py должны быть помещены в модуль ripser. 
ripser.py в репозитории - переопределенный ripser.py из стандартной библиотеки (из изменений: добавлена возможность считать метрику metric="neighbors". Эта метрика d(x, y) = позиция y среди всех соседей x. Т.е. если y - ближайший сосед, то d(x, y) = 1, для второго по отдаленности, d(x, y) = 2 etc. Это НЕ МЕТРИКА! d(x, y) != d(y, x) & транзитивности тоже нет. Так же, расчет d(x, y) зависит от других точек в датасете. По этой причине мы не можем передать эту функцию как callable в ripser/sklearn.pairwise_distance)
neighbors_distance.py на вход получает список точек. На выходе возвращает "матрицу расстояний" (опять же, эта матрица расстояний не симметрична, потому что d(x, y) не метрика в чистом виде)
function initMap() {
            // Здесь вы можете установить координаты центра карты
            var centerCoordinates = new Microsoft.Maps.Location(46.472302, 30.743517);

            // Создаем новую карту
            var map = new Microsoft.Maps.Map(document.getElementById('map'), {
                center: centerCoordinates,
                zoom: 15 // Зум карты (меняйте значение по своему усмотрению)
            });

            // Устанавливаем маркер на карте
            var marker = new Microsoft.Maps.Pushpin(centerCoordinates, {
                title: 'Мы здесь!' // Название маркера (можете изменить на свое)
            });

            // Добавляем маркер на карту
            map.entities.push(marker);
        }
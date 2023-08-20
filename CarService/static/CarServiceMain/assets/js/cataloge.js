$(document).ready(function () {
        // Обработчик клика по ссылке фильтрации
        $('a[data-filter]').click(function (e) {
            e.preventDefault();

            // Очищаем активный класс у всех ссылок и применяем его к текущей ссылке
            $('a[data-filter]').removeClass('active');
            $(this).addClass('active');

            // Получаем значение атрибута data-filter и скрываем/отображаем товары
            var filterValue = $(this).data('filter');
            if (filterValue === '.all') {
                $('.features li').show();
            } else {
                $('.features li').each(function () {
                    if ($(this).is(filterValue)) {
                        $(this).show();
                    } else {
                        $(this).hide();
                    }
                });
            }
        });
    });
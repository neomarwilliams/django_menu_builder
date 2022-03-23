require('bootstrap')

$('#menu_day_{{day.id}}').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
})

$('#menu_day_{{day.id}} a[href = "#{day.id}}/{{meal.meal_name}}"]').tab('show')
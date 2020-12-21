const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

///python manage.py collectstatic to run this
setTimeout(() => {
    $('#message').fadeOut('slow')
}, 2000);
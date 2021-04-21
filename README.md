# fnb

1. Clone repo
1. Install and start docker desktop
1. Run `docker-compose build`
1. Run `docker-compose run web python manage.py migrate`
1. Run `docker-compose up`
1. Run `docker-compose run web python manage.py createuser -is_super True -email <your email> -password <your password>`
1. Go to <localhost:8000/admin> to login to django admin
1. Go to <localhost:8000/people/login> to login to client app

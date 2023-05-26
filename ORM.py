# 1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).

user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# 2. Создать два объекта модели Author, связанные с пользователями.

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# 3. Добавить 4 категории в модель Category.

category1 = Category.objects.create(name='Sport')
category2 = Category.objects.create(name='Politics')
category3 = Category.objects.create(name='Education')
category4 = Category.objects.create(name='Technology')

# 4. Добавить 2 статьи и 1 новость.

article1 = Post.objects.create(author=author1, post_type='Article', title='Заголовок статьи 1', text='Текст статьи 1')
article2 = Post.objects.create(author=author2, post_type='Article', title='Заголовок статьи 2', text='Текст статьи 2')
news1 = Post.objects.create(author=author1, post_type='News', title='Заголовок новости', text='Текст новости')

# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

article1.categories.add(category4, category3)
article2.categories.add(category4, category2)
news1.categories.add(category1, category2)

# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

comment1 = Comment.objects.create(post=article1, user=user1, text='Комментарий к статье 1')
comment2 = Comment.objects.create(post=article2, user=user2, text='Комментарий к статье 2')
comment3 = Comment.objects.create(post=news1, user=user1, text='Комментарий к новости')
comment4 = Comment.objects.create(post=news2, user=user2, text='Комментарий к новости')

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

comment1.like()
comment2.like()
comment2.like()
comment3.dislike()
article1.like()
article2.like()

# 8. Обновить рейтинги пользователей.

author1.update_rating()
author2.update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

best_author = Author.objects.order_by('-rating').first()
print(best_author.user.username, best_author.rating)

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

best_post = Post.objects.filter(post_type='Article').order_by('-rating').first()
print(best_post.created_date, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(comment.created_date, comment.user.username, comment.rating, comment.text)

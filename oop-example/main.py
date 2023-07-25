from User import User
from Comment import Comment
from Article import Article


# Create new user

new_user = User(
    "Irving", "Suarez", "some_email@some_domain.com", "super_hyper_secure_password"
)


new_user.save()

all_users = new_user.get_all()

print(f"These are all the users: {all_users}")


# Create new Article

new_article = Article(
    "New article",
    "some contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome content",
    "posted",
    "https://cdn2.thecatapi.com/images/bom.jpg",
    "Irving",
)


new_article.save()

all_articles = new_article.get_all()

print(f"These are all the articles: {all_articles}")

# Create new Comment

new_comment = Comment(
    "some contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome contentsome content",
    "Irving",
    "New article",
)


new_comment.save()

all_comments = new_comment.get_all()

print(f"These are all the comments: {all_comments}")
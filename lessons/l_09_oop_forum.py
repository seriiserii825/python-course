from typing_extensions import List


def l_09_oop_forum():
    class User:
        def __init__(self, username: str, email: str) -> None:
            self.username = username
            self.email = email

    class Post:
        def __init__(self, title: str, content: str, author: User) -> None:
            self.title = title
            self.content = content
            self.author = author

    class Forum:
        def __init__(self) -> None:
            self.users: List[User] = []
            self.posts = []

        def register_user(self, username, email):
            user = User(username=username, email=email)
            self.users.append(user)

        def create_post(self, title, content, author):
            post = Post(title=title, content=content, author=author)
            self.posts.append(post)

    forum = Forum()
    forum.register_user('Serii', 'serii@mail.com')
    forum.create_post('title', 'post content', 'serii')

    print(forum.posts)
    print(forum.users)

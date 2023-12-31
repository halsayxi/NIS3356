from typing import Dict, Optional

from crawler.models.common import *
from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class PostImage:
    src: str
    src_set: Dict[str, str]
    height: int
    width: int


@dataclass
class ActionsSummary:
    id: int
    can_act: bool
    count: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> 'ActionsSummary':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        can_act = from_bool(obj.get("can_act"))
        count = from_int(obj.get("count"))
        return ActionsSummary(id, can_act, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["can_act"] = from_bool(self.can_act)
        result["count"] = from_int(self.count)
        return result


@dataclass
class ReplyToUser:
    username: str
    name: str
    avatar_template: str

    @staticmethod
    def from_dict(obj: Any) -> 'ReplyToUser':
        assert isinstance(obj, dict)
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        return ReplyToUser(username, name, avatar_template)

    def to_dict(self) -> dict:
        result: dict = {}
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        return result


@dataclass
class Retort:
    post_id: int
    usernames: List[str]
    emoji: str

    @staticmethod
    def from_dict(obj: Any) -> 'Retort':
        assert isinstance(obj, dict)
        post_id = from_int(obj.get("post_id"))
        usernames = from_list(from_str, obj.get("usernames"))
        emoji = from_str(obj.get("emoji"))
        return Retort(post_id, usernames, emoji)

    def to_dict(self) -> dict:
        result: dict = {}
        result["post_id"] = from_int(self.post_id)
        result["usernames"] = from_list(from_str, self.usernames)
        result["emoji"] = from_str(self.emoji)
        return result


@dataclass
class Post:
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: datetime
    cooked: str
    post_number: int
    post_type: int
    updated_at: datetime
    reply_count: int
    reply_to_post_number: Optional[int]
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: int
    yours: bool
    topic_id: int
    topic_slug: str
    display_username: str
    primary_group_name: None
    flair_name: None
    flair_url: None
    flair_bg_color: None
    flair_color: None
    flair_group_id: None
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    user_title: str
    reply_to_user: Optional[ReplyToUser]
    bookmarked: bool
    raw: str
    actions_summary: List[ActionsSummary]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    hidden: bool
    trust_level: int
    deleted_at: None
    user_deleted: bool
    edit_reason: None
    can_view_edit_history: bool
    wiki: bool
    user_cakedate: datetime
    can_accept_answer: bool
    can_unaccept_answer: bool
    accepted_answer: bool
    topic_accepted_answer: bool
    retorts: List[Retort]

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)

        id = from_int(obj.get("id"))
        name = obj.get("name", None)  # 如果不存在，则默认为 None
        username = obj.get("username", None)
        avatar_template = obj.get("avatar_template", None)
        created_at = from_datetime(obj.get("created_at")) if obj.get("created_at") is not None else None
        cooked = obj.get("cooked", None)
        post_number = from_int(obj.get("post_number"))
        post_type = from_int(obj.get("post_type"))
        updated_at = from_datetime(obj.get("updated_at")) if obj.get("updated_at") is not None else None
        reply_count = from_int(obj.get("reply_count"))
        reply_to_post_number = obj.get("reply_to_post_number")  # 可能为 None
        quote_count = from_int(obj.get("quote_count"))
        incoming_link_count = from_int(obj.get("incoming_link_count"))
        reads = from_int(obj.get("reads"))
        readers_count = from_int(obj.get("readers_count"))
        score = from_float(obj.get("score"))
        yours = from_bool(obj.get("yours"))
        topic_id = from_int(obj.get("topic_id"))
        topic_slug = obj.get("topic_slug", None)
        display_username = obj.get("display_username", None)
        primary_group_name = obj.get("primary_group_name", None)
        flair_name = obj.get("flair_name", None)
        flair_url = obj.get("flair_url", None)
        flair_bg_color = obj.get("flair_bg_color", None)
        flair_color = obj.get("flair_color", None)
        flair_group_id = obj.get("flair_group_id", None)
        version = from_int(obj.get("version"))
        can_edit = from_bool(obj.get("can_edit"))
        can_delete = from_bool(obj.get("can_delete"))
        can_recover = from_bool(obj.get("can_recover"))
        can_see_hidden_post = from_bool(obj.get("can_see_hidden_post"))
        can_wiki = from_bool(obj.get("can_wiki"))
        user_title = obj.get("user_title", None)
        reply_to_user = obj.get("reply_to_user", None)  # 使用 from_union 替换
        bookmarked = from_bool(obj.get("bookmarked"))
        raw = obj.get("raw", None)
        actions_summary = obj.get("actions_summary", [])  # 空列表作为默认值
        moderator = from_bool(obj.get("moderator"))
        admin = from_bool(obj.get("admin"))
        staff = from_bool(obj.get("staff"))
        user_id = from_int(obj.get("user_id"))
        hidden = from_bool(obj.get("hidden"))
        trust_level = from_int(obj.get("trust_level"))
        deleted_at = obj.get("deleted_at", None)  # 如果不存在，则默认为 None
        user_deleted = from_bool(obj.get("user_deleted"))
        edit_reason = obj.get("edit_reason", None)
        can_view_edit_history = from_bool(obj.get("can_view_edit_history"))
        wiki = from_bool(obj.get("wiki"))
        user_cakedate = from_datetime(obj.get("user_cakedate")) if obj.get("user_cakedate") is not None else None
        can_accept_answer = from_bool(obj.get("can_accept_answer"))
        can_unaccept_answer = from_bool(obj.get("can_unaccept_answer"))
        accepted_answer = from_bool(obj.get("accepted_answer"))
        topic_accepted_answer = from_bool(obj.get("topic_accepted_answer"))
        retorts = from_list(Retort.from_dict, obj.get("retorts")) if obj.get("retorts") is not None else []

        return Post(id, name, username, avatar_template, created_at, cooked, post_number, post_type, updated_at,
                    reply_count, reply_to_post_number, quote_count, incoming_link_count, reads, readers_count, score,
                    yours, topic_id, topic_slug, display_username, primary_group_name, flair_name, flair_url,
                    flair_bg_color, flair_color, flair_group_id, version, can_edit, can_delete, can_recover,
                    can_see_hidden_post, can_wiki, user_title, reply_to_user, bookmarked, raw, actions_summary,
                    moderator, admin, staff, user_id, hidden, trust_level, deleted_at, user_deleted, edit_reason,
                    can_view_edit_history, wiki, user_cakedate, can_accept_answer, can_unaccept_answer, accepted_answer,
                    topic_accepted_answer, retorts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["username"] = from_str(self.username)
        result["avatar_template"] = from_str(self.avatar_template)
        result["created_at"] = self.created_at.isoformat()
        result["cooked"] = from_str(self.cooked)
        result["post_number"] = from_int(self.post_number)
        result["post_type"] = from_int(self.post_type)
        result["updated_at"] = self.updated_at.isoformat()
        result["reply_count"] = from_int(self.reply_count)
        result["reply_to_post_number"] = from_int(self.reply_to_post_number)
        result["quote_count"] = from_int(self.quote_count)
        result["incoming_link_count"] = from_int(self.incoming_link_count)
        result["reads"] = from_int(self.reads)
        result["readers_count"] = from_int(self.readers_count)
        result["score"] = from_float(self.score)
        result["yours"] = from_bool(self.yours)
        result["topic_id"] = from_int(self.topic_id)
        result["topic_slug"] = from_str(self.topic_slug)
        result["display_username"] = from_str(self.display_username)
        result["primary_group_name"] = from_none(self.primary_group_name)
        result["flair_name"] = from_none(self.flair_name)
        result["flair_url"] = from_none(self.flair_url)
        result["flair_bg_color"] = from_none(self.flair_bg_color)
        result["flair_color"] = from_none(self.flair_color)
        result["flair_group_id"] = from_none(self.flair_group_id)
        result["version"] = from_int(self.version)
        result["can_edit"] = from_bool(self.can_edit)
        result["can_delete"] = from_bool(self.can_delete)
        result["can_recover"] = from_bool(self.can_recover)
        result["can_see_hidden_post"] = from_bool(self.can_see_hidden_post)
        result["can_wiki"] = from_bool(self.can_wiki)
        result["user_title"] = from_str(self.user_title)
        result["reply_to_user"] = to_class(ReplyToUser, self.reply_to_user)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["raw"] = from_str(self.raw)
        result["actions_summary"] = from_list(
            lambda x: to_class(ActionsSummary, x), self.actions_summary)
        result["moderator"] = from_bool(self.moderator)
        result["admin"] = from_bool(self.admin)
        result["staff"] = from_bool(self.staff)
        result["user_id"] = from_int(self.user_id)
        result["hidden"] = from_bool(self.hidden)
        result["trust_level"] = from_int(self.trust_level)
        result["deleted_at"] = from_none(self.deleted_at)
        result["user_deleted"] = from_bool(self.user_deleted)
        result["edit_reason"] = from_none(self.edit_reason)
        result["can_view_edit_history"] = from_bool(self.can_view_edit_history)
        result["wiki"] = from_bool(self.wiki)
        result["user_cakedate"] = self.user_cakedate.isoformat()
        result["can_accept_answer"] = from_bool(self.can_accept_answer)
        result["can_unaccept_answer"] = from_bool(self.can_unaccept_answer)
        result["accepted_answer"] = from_bool(self.accepted_answer)
        result["topic_accepted_answer"] = from_bool(self.topic_accepted_answer)
        result["retorts"] = from_list(Retort.from_dict, self.retorts)
        return result

    def get_imgs(self) -> List[PostImage]:
        soup = BeautifulSoup(self.cooked, 'html.parser')
        imgs = soup.find_all("img", attrs={"src": True})
        ret = []
        for img in imgs:
            src = img.get("src")
            src_set_attr: str = img.get("srcset")
            src_set_parts = src_set_attr.split(',')
            src_set = {}
            for part in src_set_parts:
                part = part.strip()
                pair = part.split(' ')
                if len(pair) == 2:
                    url, times = pair[0], pair[1]
                    src_set[times] = url
            height_attr: str = img.get("height")
            width_attr: str = img.get("width")
            height = width = 0
            if height_attr.isdigit():
                height = int(height_attr)
            if width_attr.isdigit():
                width = int(width_attr)
            ret.append(PostImage(src, src_set, height, width))

        return ret


def post_from_dict(s: Any) -> Post:
    return Post.from_dict(s)


def post_to_dict(x: Post) -> Any:
    return to_class(Post, x)

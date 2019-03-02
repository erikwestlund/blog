from flask import jsonify
from sqlalchemy import desc
from utils.models.json_encoder import AlchemyEncoder


def paginated_json_response(
    model="",
    url="",
    page=1,
    per_page=20,
    order_by=None,
    order_by_direction="asc",
    left_edge=2,
    left_current=2,
    right_current=3,
    right_edge=2,
    user_id=None,
    query=None,
):
    if not query:
        query = model.query

        if order_by and order_by_direction == "asc":
            query = query.order_by(order_by)
        elif order_by and order_by_direction == "desc":
            query = query.order_by(desc(order_by))

        if user_id:
            query = query.filter_by(user_id=user_id)

    paginated = query.paginate(page=page, per_page=per_page)

    items_from = ((paginated.page - 1) * per_page) + 1
    items_to = paginated.page * per_page

    return jsonify(
        {
            "meta": {
                "pagination": {
                    "from": items_from,
                    "to": items_to,
                    "total": paginated.total,
                    "per_page": paginated.per_page,
                    "prev_page": paginated.prev_num,
                    "current_page": paginated.page,
                    "next_page": paginated.next_num,
                    "last_page": paginated.pages,
                    "has_next": paginated.has_next,
                    "has_prev": paginated.has_prev,
                    "page_list": [
                        page
                        for page in paginated.iter_pages(
                            left_edge=left_edge,
                            left_current=left_current,
                            right_edge=right_edge,
                            right_current=right_current,
                        )
                    ],
                    "base_url": url,
                    "first_page_url": url + "?page=1",
                    "last_page_url": url + "?page=" + str(paginated.pages),
                    "prev_page_url": url + "?page=" + str(paginated.prev_num)
                    if paginated.has_prev
                    else None,
                    "next_page_url": url + "?page=" + str(paginated.next_num)
                    if paginated.has_next
                    else None,
                }
            },
            "data": paginated.items,
        }
    )

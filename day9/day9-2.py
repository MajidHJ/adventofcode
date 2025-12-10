import math

spath = 'day9/sample.txt'
ipath = 'day9/input.txt'
path = ipath


from typing import List, Tuple

Point = Tuple[int,int]
Edge = Tuple[Point,Point]

def edges_from_polygon(poly: List[Point]) -> List[Edge]:
    return [ (poly[i], poly[(i+1)%len(poly)]) for i in range(len(poly)) ]

def point_on_segment(a: Point, b: Point, p: Point) -> bool:
    """
    Return True if p lies on the closed segment [a,b].
    Works for axis-aligned segments but also general (using cross and bbox).
    All integer arithmetic.
    """
    (x1,y1),(x2,y2) = a,b
    (x,y) = p
    # bounding box check
    if not (min(x1,x2) <= x <= max(x1,x2) and min(y1,y2) <= y <= max(y1,y2)):
        return False
    # collinearity: (p-a) x (b-a) == 0
    cross = (x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)
    return cross == 0

def point_in_polygon(pt: Point, poly: List[Point], allow_on_boundary: bool = True) -> bool:
    """
    Ray-casting to the +x direction. Because polygon is orthogonal,
    intersection x-coordinate equals vertical-edge x when edge is vertical.
    If point lies exactly on any polygon edge -> return allow_on_boundary.
    """
    x,y = pt
    n = len(poly)
    inside = False
    for i in range(n):
        x1,y1 = poly[i]
        x2,y2 = poly[(i+1)%n]
        # boundary check: if pt exactly on edge
        if point_on_segment((x1,y1),(x2,y2),(x,y)):
            return allow_on_boundary
        # count intersections of ray (y constant, x -> +inf) with edge
        # only edges that cross the horizontal line at y (strictly one endpoint above, one below)
        if (y1 > y) != (y2 > y):
            # For orthogonal polygon vertical edges give x_intersection = x1
            if x1 == x2:
                x_int = x1
            else:
                # should not happen for pure orthogonal, but handle safely (rational)
                # compute as fraction, compare with x without floating point:
                # x_int = x1 + (x2-x1)*(y-y1)/(y2-y1)
                # we only need to know if x_int > x: compare (x1*(y2-y1) + (x2-x1)*(y-y1)) ? x*(y2-y1)
                num = x1*(y2-y1) + (x2-x1)*(y-y1)
                den = (y2-y1)
                if den > 0:
                    if num > x*den:
                        inside = not inside
                else:
                    if num < x*den:
                        inside = not inside
                continue
            if x_int > x:
                inside = not inside
    return inside

def seg_intersection_type(a1:Point,a2:Point,b1:Point,b2:Point) -> str:
    """
    Return one of: 'none', 'point', 'overlap'
    Assumes segments are axis-aligned (but works generally for detection).
    - 'none' : no intersection
    - 'point': intersection at a single point
    - 'overlap': collinear overlapping with segment length > 0
    """
    # quick bbox reject
    if max(a1[0], a2[0]) < min(b1[0], b2[0]) or max(b1[0], b2[0]) < min(a1[0], a2[0]) or \
       max(a1[1], a2[1]) < min(b1[1], b2[1]) or max(b1[1], b2[1]) < min(a1[1], a2[1]):
        return 'none'
    # check collinear (cross products zero for endpoints)
    def cross(u,v,w):
        # cross of (v-u) x (w-u)
        return (v[0]-u[0])*(w[1]-u[1]) - (v[1]-u[1])*(w[0]-u[0])
    if cross(a1,a2,b1) == 0 and cross(a1,a2,b2) == 0:
        # collinear -> check overlap length
        # project on x if not vertical, else on y
        if a1[0] != a2[0]:
            a_min,a_max = min(a1[0],a2[0]), max(a1[0],a2[0])
            b_min,b_max = min(b1[0],b2[0]), max(b1[0],b2[0])
        else:
            a_min,a_max = min(a1[1],a2[1]), max(a1[1],a2[1])
            b_min,b_max = min(b1[1],b2[1]), max(b1[1],b2[1])
        if a_max < b_min or b_max < a_min:
            return 'none'
        # if they touch at a single endpoint (zero-length overlap) it's still 'point'
        overlap_len = min(a_max,b_max) - max(a_min,b_min)
        if overlap_len > 0:
            return 'overlap'
        else:
            return 'point'
    # not collinear: check if they cross at a single point
    # For axis-aligned, one vertical and one horizontal -> intersection if vertical.x in horiz.x-range and horiz.y in vert.y-range
    if a1[0]==a2[0] and b1[1]==b2[1]:
        xa = a1[0]; yb = b1[1]
        if min(b1[0],b2[0]) <= xa <= max(b1[0],b2[0]) and min(a1[1],a2[1]) <= yb <= max(a1[1],a2[1]):
            return 'point'
        else:
            return 'none'
    if a1[1]==a2[1] and b1[0]==b2[0]:
        ya = a1[1]; xb = b1[0]
        if min(a1[0],a2[0]) <= xb <= max(a1[0],a2[0]) and min(b1[1],b2[1]) <= ya <= max(b1[1],b2[1]):
            return 'point'
        else:
            return 'none'
    # general intersection test (shouldn't be needed for orthogonal, but safe)
    # Using orientation tests
    def orient(p,q,r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
    o1 = orient(a1,a2,b1)
    o2 = orient(a1,a2,b2)
    o3 = orient(b1,b2,a1)
    o4 = orient(b1,b2,a2)
    if o1==0 and point_on_segment(a1,a2,b1): return 'point'
    if o2==0 and point_on_segment(a1,a2,b2): return 'point'
    if o3==0 and point_on_segment(b1,b2,a1): return 'point'
    if o4==0 and point_on_segment(b1,b2,a2): return 'point'
    if (o1>0) != (o2>0) and (o3>0) != (o4>0):
        return 'point'
    return 'none'

def rectangle_inside_orthogonal_polygon(poly: List[Point],
                                        corner1: Point,
                                        corner2: Point,
                                        allow_touch: bool = True) -> bool:
    """
    Main check. allow_touch=True means touching/overlap is permitted.
    Steps:
      1) check four corners are inside or on boundary (depending on allow_touch)
      2) check rectangle edges do not have an interior intersection with polygon edges
         (i.e., an intersection point that lies in interior of both segments) -> reject
      3) optional safety: check a sample interior point of rectangle is inside
    Complexity: O(n) where n = number of polygon edges.
    """
    xmin,xmax = min(corner1[0],corner2[0]), max(corner1[0],corner2[0])
    ymin,ymax = min(corner1[1],corner2[1]), max(corner1[1],corner2[1])
    rect_corners = [(xmin,ymin),(xmin,ymax),(xmax,ymin),(xmax,ymax)]
    # 1) corners
    for p in rect_corners:
        if not point_in_polygon(p, poly, allow_on_boundary=allow_touch):
            return False
    # 2) check edge intersections
    rect_edges = [
        ((xmin,ymin),(xmax,ymin)),
        ((xmin,ymax),(xmax,ymax)),
        ((xmin,ymin),(xmin,ymax)),
        ((xmax,ymin),(xmax,ymax))
    ]
    poly_edges = edges_from_polygon(poly)
    for re in rect_edges:
        for pe in poly_edges:
            itype = seg_intersection_type(re[0],re[1], pe[0],pe[1])
            if itype == 'none':
                continue
            if itype == 'overlap':
                # overlap is allowed when allow_touch==True
                if not allow_touch:
                    return False
                else:
                    continue
            if itype == 'point':
                # find the intersection point(s). For axis-aligned case it's straightforward.
                # compute intersection coordinate
                # if intersection point is interior to both segments => reject
                # endpoints are allowed when allow_touch True
                # We'll test: intersection point equals an endpoint of rectangle edge or polygon edge?
                # If equal to an endpoint of either but interior to the other -> still allowed (touch)
                # Only reject if it is interior to BOTH.
                # Determine if intersection == interior point for re and pe
                # For axis-aligned: intersection coordinates:
                ax1,ay1 = re[0]; ax2,ay2 = re[1]
                bx1,by1 = pe[0]; bx2,by2 = pe[1]
                # find intersection point by scanning possibilities
                inter_points = []
                # check endpoints equality
                candidates = [re[0], re[1]]
                for c in candidates:
                    if point_on_segment(pe[0], pe[1], c):
                        inter_points.append(c)
                candidates = [pe[0], pe[1]]
                for c in candidates:
                    if point_on_segment(re[0], re[1], c):
                        inter_points.append(c)
                # if none of endpoints lies on the other, then it's interior-intersection
                if len(inter_points) == 0:
                    # interior to both => reject regardless of allow_touch
                    return False
                else:
                    # all intersection points are at endpoints (touches) -> allowed when allow_touch True
                    if not allow_touch:
                        # if any intersection point is an endpoint but lies strictly inside other => still intersection => reject
                        # but for simplicity, reject
                        return False
                    # else allowed; continue
                    continue
    # 3) sample interior point check (safe-guard)
    # choose a point strictly inside rectangle: (xmin + 1, ymin + 1) etc may fail if width=0 or height=0
    if xmin == xmax or ymin == ymax:
        # degenerate rectangle (line or point). corners already checked; accept if corners were allowed
        return True
    # pick center as rational; choose integer interior if possible
    cx = xmin + (xmax - xmin) // 2
    cy = ymin + (ymax - ymin) // 2
    if not point_in_polygon((cx,cy), poly, allow_on_boundary=allow_touch):
        return False
    return True

def area_vector(points):
    n = len(points)
    dist = []
    for i in range(n):
        for j in range(i+1,n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            a = math.fabs(x1-x2+1)*math.fabs(y1-y2+1)
            dist.append((i,j,int(a)))

    return dist




if __name__ == "__main__":

    with open(path) as f:
        poly = ([list(map(int,i.strip().split(','))) for i in f])     
    area = area_vector(poly)
    area.sort(key=lambda x: x[2],reverse=True)
    for i in area:
        a,b,c = i
        a = poly[a]
        b = poly[b]
        ok = rectangle_inside_orthogonal_polygon(poly, a, b, allow_touch=True)
        print(f"rect {a} - {b} -> inside? {ok}")
        # if ok : break
# print(a,b,c)
# print(c)


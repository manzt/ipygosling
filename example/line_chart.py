import gosling as gos

data = gos.Data(
    url="https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
    type="multivec",
    row="sample",
    column="position",
    value="peak",
    categories=["sample 1"],
    binSize=5,
)

domain = gos.Domain(chromosome="1", interval=[1, 30005000])

track = gos.Track(data).mark_line().encode(
    x=gos.Channel("position:G", domain=domain, axis="bottom"),
    y="peak:Q",
    size=gos.value(2),
).properties(layout="linear", width=800, height=180)

track.view(title="Basic Marks: Line", subtitle="Tutorial Examples")
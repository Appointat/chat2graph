from typing import Dict, List, Optional, Union
from uuid import uuid4

from app.core.toolkit.tool import Tool
from app.plugin.neo4j.neo4j_store import get_neo4j
from app.plugin.neo4j.resource.read_doc import SchemaManager

DOC_CONTENT = """
# 罗密欧与朱丽叶：故事梗概与人物关系

## 背景

故事发生在意大利维罗纳城。维罗纳城中有两个世代为敌的家族：蒙太古家族和凯普莱特家族。两个家族之间的仇恨由来已久，其成员经常在城中发生冲突。

## 主要人物及关系

1. **罗密欧**：蒙太古家族的儿子，年轻的贵族。
2. **朱丽叶**：凯普莱特家族的女儿，14岁。
3. **蒙太古先生**：罗密欧的父亲，蒙太古家族的家主。
4. **蒙太古夫人**：罗密欧的母亲。
5. **凯普莱特先生**：朱丽叶的父亲，凯普莱特家族的家主。
6. **凯普莱特夫人**：朱丽叶的母亲。
7. **茂丘西奥**：罗密欧的好友，维罗纳王子的亲戚。
8. **班伏里奥**：罗密欧的表兄，也是蒙太古家族成员。
9. **提拜尔特**：朱丽叶的表兄，凯普莱特家族成员。
10. **朱丽叶的奶妈**：朱丽叶的照料者和保密者。
11. **神父劳伦斯**：维罗纳的方济各会神父，同时是罗密欧的精神顾问。
12. **巴黎伯爵**：贵族，想要娶朱丽叶的求婚者。
13. **巴尔萨扎**：罗密欧的忠实仆人。
14. **埃斯卡勒斯王子**：维罗纳的统治者，对两家的争斗感到厌烦。

## 故事情节

### 第一部分：初次相遇

1. 维罗纳城内，蒙太古和凯普莱特两家的仆人在街头发生争斗。埃斯卡勒斯王子出面制止，并宣布如再次发生冲突，参与者将被处死。

2. 罗密欧当时正为一位叫罗瑟琳的女子的拒绝而伤心。

3. 班伏里奥建议罗密欧去参加凯普莱特家举办的舞会，以忘记罗瑟琳。

4. 同一时间，凯普莱特夫人告诉朱丽叶，巴黎伯爵想要娶她，并且凯普莱特先生已经同意。朱丽叶表示她从未想过婚姻。

5. 罗密欧、班伏里奥和茂丘西奥戴着面具潜入凯普莱特家的舞会。在舞会上，罗密欧一眼看见朱丽叶就爱上了她。

6. 罗密欧与朱丽叶交谈并跳舞。后来罗密欧才知道朱丽叶是凯普莱特家的女儿，朱丽叶也得知罗密欧是蒙太古家的儿子。

7. 舞会结束后，罗密欧不愿离去，偷偷溜到凯普莱特家的花园里。他听到朱丽叶在阳台上自言自语，表达对他的感情，并为他是蒙太古家的人而苦恼。

8. 罗密欧现身，两人互诉爱意，约定第二天秘密结婚。

### 第二部分：秘密婚礼与冲突升级

1. 次日，罗密欧去找神父劳伦斯，请求他为他和朱丽叶主持婚礼。神父劳伦斯同意，希望通过这段婚姻结束两家的仇恨。

2. 朱丽叶借口去教堂忏悔，与罗密欧在神父劳伦斯的见证下秘密结婚。

3. 婚礼后，罗密欧在街头遇到提拜尔特。提拜尔特因罗密欧闯入舞会而愤怒，挑衅罗密欧。罗密欧因刚与朱丽叶结婚，拒绝与提拜尔特决斗。

4. 茂丘西奥误以为罗密欧是懦弱，替罗密欧应战。在打斗中，罗密欧试图阻止两人，却导致茂丘西奥被提拜尔特刺伤致死。

5. 罗密欧因好友之死愤怒，杀死了提拜尔特，随后逃离现场。

6. 埃斯卡勒斯王子听取事件经过后，判处罗密欧终身流放，如再踏入维罗纳一步就处死。

### 第三部分：分离与计划

1. 朱丽叶得知表兄提拜尔特被罗密欧杀死的消息，陷入两难境地：既为表兄之死悲痛，又担心丈夫的命运。

2. 神父劳伦斯安排罗密欧在离开维罗纳前与朱丽叶见最后一面。两人在朱丽叶的房间度过最后一晚，黎明前罗密欧离开，前往曼图亚。

3. 凯普莱特先生为使朱丽叶走出悲伤，决定加速她与巴黎伯爵的婚事，定在三天后举行。

4. 朱丽叶拒绝这门婚事，凯普莱特先生勃然大怒，威胁要与女儿断绝关系。

5. 绝望的朱丽叶去找神父劳伦斯寻求帮助。神父给了她一种药水，饮用后会让她看似死亡，实则只是深度睡眠，持续42小时。

6. 神父的计划是：朱丽叶假死后会被安放在家族墓穴，神父会通知罗密欧这个计划，让他在朱丽叶醒来时前来接她，两人一起逃往曼图亚。

7. 朱丽叶回家后，假装同意与巴黎伯爵的婚事，实则在婚礼前夜喝下了药水，陷入假死状态。

### 第四部分：误会与悲剧

1. 朱丽叶被发现"死"在床上，原定的婚礼变成了葬礼。她被安放在凯普莱特家的墓穴中。

2. 神父劳伦斯派一位修士前往曼图亚告知罗密欧计划，但因城中爆发瘟疫，修士被隔离，未能及时送达信件。

3. 罗密欧的仆人巴尔萨扎得知朱丽叶"死亡"的消息，立即赶到曼图亚告诉罗密欧。

4. 罗密欧以为朱丽叶真的死了，买了一瓶毒药，决定回到维罗纳与朱丽叶同死。

5. 罗密欧回到维罗纳，在墓穴外遇到前来悼念朱丽叶的巴黎伯爵。两人决斗，罗密欧杀死了巴黎伯爵。

6. 罗密欧进入墓穴，看到"死去"的朱丽叶，喝下毒药自杀。

7. 朱丽叶醒来，发现罗密欧已死，悲痛欲绝。神父劳伦斯赶到墓穴，试图带走朱丽叶，但她拒绝离开。

8. 神父听到巡逻队的脚步声不得不离开。朱丽叶拿起罗密欧的匕首，刺入自己的胸膛，死在罗密欧身边。

### 第五部分：和解

1. 巡逻队发现了罗密欧、朱丽叶和巴黎伯爵三具尸体。蒙太古家和凯普莱特家的人都赶到墓穴。

2. 神父劳伦斯讲述了事情的经过，两家族长意识到他们多年的仇恨导致了这场悲剧。

3. 蒙太古先生和凯普莱特先生决定结束两家的仇恨，在维罗纳广场上为罗密欧和朱丽叶建立一座金像，作为和解的象征。

4. 自此，两家的仇恨结束，维罗纳城恢复和平。

## 关键关系概述

1. **家族关系**：
   - 罗密欧是蒙太古家族的儿子
   - 朱丽叶是凯普莱特家族的女儿
   - 蒙太古家族和凯普莱特家族是世仇

2. **爱情关系**：
   - 罗密欧爱上朱丽叶
   - 朱丽叶爱上罗密欧
   - 巴黎伯爵求娶朱丽叶

3. **友谊关系**：
   - 班伏里奥是罗密欧的表兄和朋友
   - 茂丘西奥是罗密欧的好友
   - 提拜尔特是朱丽叶的表兄

4. **辅助关系**：
   - 神父劳伦斯帮助罗密欧和朱丽叶
   - 朱丽叶的奶妈是朱丽叶的支持者
   - 巴尔萨扎是罗密欧的忠实仆人

5. **权力关系**：
   - 埃斯卡勒斯王子是维罗纳的统治者
   - 凯普莱特先生对朱丽叶有决定权
   - 蒙太古先生是罗密欧的父亲

## 主要事件顺序

1. 两家族仆人街头斗殴
2. 罗密欧参加凯普莱特家舞会
3. 罗密欧与朱丽叶相爱
4. 罗密欧与朱丽叶秘密结婚
5. 罗密欧杀死提拜尔特
6. 罗密欧被流放
7. 朱丽叶被迫答应嫁给巴黎伯爵
8. 朱丽叶服药假死
9. 罗密欧误信朱丽叶死讯
10. 罗密欧自杀
11. 朱丽叶自杀
12. 两家族和解

## 原因与结果链

1. 因为两家族的仇恨，所以罗密欧和朱丽叶的爱情被阻碍
2. 因为罗密欧参加舞会，所以他遇见并爱上朱丽叶
3. 因为提拜尔特杀死茂丘西奥，所以罗密欧杀死提拜尔特
4. 因为罗密欧杀死提拜尔特，所以他被流放
5. 因为罗密欧被流放，所以朱丽叶被迫嫁给巴黎伯爵
6. 因为朱丽叶不想嫁给巴黎伯爵，所以她服药假死
7. 因为信件未送达，所以罗密欧误以为朱丽叶真死了
8. 因为罗密欧以为朱丽叶死了，所以他自杀
9. 因为罗密欧自杀，所以朱丽叶也自杀
10. 因为罗密欧和朱丽叶的死，所以两家族最终和解
"""  # noqa: E501


class DocumentReader(Tool):
    """Tool for analyzing document content."""

    def __init__(self, id: Optional[str] = None):
        super().__init__(
            id=id or str(uuid4()),
            name=self.read_document.__name__,
            description=self.read_document.__doc__ or "",
            function=self.read_document,
        )

    async def read_document(self, doc_name: str, chapter_name: str) -> str:
        """Read the document content given the document name and chapter name.

        Args:
            doc_name (str): The name of the document.
            chapter_name (str): The name of the chapter of the document.

        Returns:
            The content of the document.
        """

        return DOC_CONTENT


class VertexLabelGenerator(Tool):
    """Tool for generating Cypher statements to create vertex labels in Neo4j."""

    def __init__(self, id: Optional[str] = None):
        super().__init__(
            id=id or str(uuid4()),
            name=self.create_vertex_label_by_json_schema.__name__,
            description=self.create_vertex_label_by_json_schema.__doc__ or "",
            function=self.create_vertex_label_by_json_schema,
        )

    async def create_vertex_label_by_json_schema(
        self,
        label: str,
        properties: List[Dict[str, Union[str, bool]]],
        primary: str = "id",
    ) -> str:
        """Create a vertex label in Neo4j with specified properties.

        This function defines a new vertex label (node type) in the Neo4j graph database,
        establishing its property schema and primary key.

        Args:
            label (str): The label name for the vertex type. Must be a valid Neo4j label name.
            properties (List[Dict[str, Union[str, bool]]]): Property definitions for the label.
                Each property is defined as a dictionary containing:
                    - name (str): Property name
                    - type (str): Data type (e.g., 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN',
                        'DATE', 'DATETIME')
                    - index (bool): Whether to create an index for the property (default: True)
            primary (str): The property name to be used as the primary key. Must be unique
                within the label (default: 'id').

        Returns:
            str: Status message indicating successful label creation with constraint and
                index details.

        Example:
            ```python
            properties = [
                {
                    "name": "id",
                    "type": "STRING",
                    "index": True,
                },
                {
                    "name": "name",
                    "type": "STRING",
                    "index": False,
                }
            ]
            result = await create_vertex_label_by_json_schema("Person", properties, "id")
            ```
        """

        statements = []

        statements.append(
            f"CREATE CONSTRAINT {label.lower()}_{primary}_unique IF NOT EXISTS "
            f"FOR (n:{label}) REQUIRE n.{primary} IS UNIQUE"
        )

        # create indexes for other properties
        for prop in properties:
            if prop.get("index", True) and prop["name"] != primary:
                statements.append(
                    f"CREATE INDEX {label}_{prop['name']}_idx IF NOT EXISTS "
                    f"FOR (n:{label}) ON (n.{prop['name']})"
                )

        # prepare schema information
        property_details = []
        for p in properties:
            property_details.append(
                {
                    "name": p["name"],
                    "type": p["type"],
                    "has_index": p.get("index", True),
                    "index_name": f"{label}_{p['name']}_idx" if p.get("index", True) else None,
                }
            )

        store = get_neo4j()
        with store.conn.session() as session:
            for statement in statements:
                print(f"Executing statement: {statement}")
                session.run(statement)

            # update schema file
            schema = await SchemaManager.read_schema()
            schema["nodes"][label] = {"primary_key": primary, "properties": property_details}
            await SchemaManager.write_schema(schema)

            return f"Successfully created label {label}"


class EdgeLabelGenerator(Tool):
    """Tool for generating Cypher statements to create edge labels in TuGraph."""

    def __init__(self, id: Optional[str] = None):
        super().__init__(
            id=id or str(uuid4()),
            name=self.create_edge_label_by_json_schema.__name__,
            description=self.create_edge_label_by_json_schema.__doc__ or "",
            function=self.create_edge_label_by_json_schema,
        )

    async def create_edge_label_by_json_schema(
        self,
        label: str,
        properties: List[Dict[str, Union[str, bool]]],
        primary: str = "id",
    ) -> str:
        """Create a relationship type in Neo4j with specified properties.

        This function defines a new relationship type in the Neo4j graph database,
        establishing its property schema, and valid node label pairs
        for the relationship endpoints.

        Args:
            label (str): The label name for the relationship type. Will be automatically
                converted to uppercase as per Neo4j conventions.
            properties (List[Dict[str, Union[str, bool]]]): Property definitions for the
                relationship type. Each property is defined as a dictionary containing:
                    - name (str): Property name
                    - type (str): Data type (e.g., 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN',
                        'DATE', 'DATETIME')
                    - index (bool): Whether to create an index for the property (default: True)
            primary (str): The property name to be used as the unique identifier. Must be
                unique within the relationship type (default: 'id').

        Returns:
            str: Status message indicating successful relationship type creation with
                constraint and index details.

        Example:
            ```python
            properties = [
                {
                    "name": "participate",
                    "type": "STRING",
                    "index": True,
                },
                {
                    "name": "since",
                    "type": "DATETIME",
                    "index": False,
                }
            ]
            result = await create_edge_label_by_json_schema(
                "WORKS_FOR", properties, "id"
            )
            ```
        """
        label = label.upper()
        statements = []

        # create the constraints for the relationship
        statements.append(
            f"CREATE CONSTRAINT {label.lower()}_{primary}_unique IF NOT EXISTS "
            f"FOR ()-[r:{label}]-() "
            f"REQUIRE r.{primary} IS UNIQUE"
        )

        # create indexes for other properties
        for prop in properties:
            if prop.get("index", True) and prop["name"] != primary:
                statements.append(
                    f"CREATE INDEX {label}_{prop['name']}_idx IF NOT EXISTS "
                    f"FOR ()-[r:{label}]-() ON (r.{prop['name']})"
                )

        # prepare schema information
        property_details = []
        for p in properties:
            property_details.append(
                {
                    "name": p["name"],
                    "type": p["type"],
                    "has_index": p.get("index", True),
                    "index_name": f"{label}_{p['name']}_idx" if p.get("index", True) else None,
                }
            )

        store = get_neo4j()
        with store.conn.session() as session:
            for statement in statements:
                print(f"Executing statement: {statement}")
                session.run(statement)

        # update schema file
        schema = await SchemaManager.read_schema()
        schema["relationships"][label] = {"primary_key": primary, "properties": property_details}
        await SchemaManager.write_schema(schema)

        return f"Successfully configured relationship type {label}"


class GraphReachabilityGetter(Tool):
    """Tool for getting the reachability information of the graph database."""

    def __init__(self, id: Optional[str] = None):
        super().__init__(
            id=id or str(uuid4()),
            name=self.get_graph_reachability.__name__,
            description=self.get_graph_reachability.__doc__ or "",
            function=self.get_graph_reachability,
        )

    async def get_graph_reachability(self) -> str:
        """Get the reachability information of the graph database which can help to understand the
        graph structure.

        Args:
            None args required

        Returns:
            str: The reachability of the graph database in string format
        """
        store = get_neo4j()
        vertex_labels: List = []
        relationship_types: List = []
        with store.conn.session() as session:
            # get all vertex labels
            result = session.run("""
                CALL db.labels() YIELD label 
                RETURN collect(label) as labels
            """)
            vertex_labels = result.single()["labels"]

            # get all relationship types and their connected node labels
            result = session.run("""
                CALL db.relationshipTypes() YIELD relationshipType
                RETURN collect(relationshipType) as types
            """)
            relationship_types = result.single()["types"]

        return (
            "Here is the schema, you have to check if there exists at least one edge label between "
            "two vertex labels! If no, create more edges to make the graph more connected.\n"
            f"Vertex labels: {vertex_labels}\nRelationship types: {relationship_types}"
        )

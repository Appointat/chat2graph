from chat2graph.core.model.message import HybridMessage, TextMessage
from chat2graph.core.sdk.agentic_service import AgenticService


def main():
    """Main function."""
    mas = AgenticService.load("test/example/coding_system/code_system.yml")

    # set the user message
    user_message = TextMessage(
        #         payload="""
        # 开发一个贪吃蛇游戏。游戏的核心玩法应包含蛇的移动、通过吃食物实现身体增长，以及撞到墙壁或自身导致游戏结束的基础机制。为增加挑战与趣味性，游戏需提供至少三个难度等级，这些等级可以影响蛇的移动速度、食物的刷新率等方面。此外，应引入多样化的游戏元素，具体包括实现2-3种具有特殊效果的食物或道具（例如，能获得更高分数的高分食物、使蛇减速的道具、或提供临时无敌的护盾），并在游戏区域内设置障碍物以增加游戏难度。计分系统应由基础得分与额外的奖励得分构成。游戏模式方面，至少应包含经典的无尽模式，并可考虑加入逐步解锁或具有特定目标的关卡模式。
        # 在界面与视觉设计(UI/UX)方面，游戏整体应采用现代简约的风格。所有视觉元素，包括蛇的造型、食物与道具的设计、游戏区域的划分，以及用户界面（如显示得分、当前长度、游戏开始/结束/暂停等状态的界面），都必须设计得清晰美观。用户的操作，如蛇的移动、吃到食物、以及游戏结束等事件，均需配有流畅的动画效果和即时的视觉反馈，以提升用户体验。
        # AI玩家的设计是本项目的核心挑战，其目标是能够自主进行游戏，并以追求长时间存活和获得高分为导向，力求达到“完美游戏”的水平。为实现此目标，AI必须具备智能的路径规划核心能力，例如运用A*或BFS等算法来高效地寻找并吃到食物，同时能完美避开所有障碍物及其自身的身体。推荐为AI集成更高级的策略，包括能够评估并选择当前最优的食物目标，具备一定的长远规划能力（例如，可以借鉴类似“汉密尔顿回路”的思路来尽可能填满空间，避免自我困死），并将长期生存置于短期得分利益之上。游戏应提供观看AI进行游戏的功能，并能一定程度上可视化其决策过程或路径规划思路。
        #         """
        payload="""
目标：构建图社区发现的算法演示程序。
步骤：
1. 生成图数据：100 个节点、2000 条边；点的度数分布满足幂律分布。
2. 执行某 **一个** 图社区发现算法，如 LPA、leiden、louvain 等。
3. 可视化图数据，合理布局，使用不同颜色高亮展示每一个图社区。
4. 循环以上过程，请注意迭代间隔，方便用户观察。

拆解成 1 个 subtask，就够了。
        """
    )

    # submit the job
    service_message = mas.session().submit(user_message).wait()

    # print the result
    if isinstance(service_message, TextMessage):
        print(f"Service Result:\n{service_message.get_payload()}")
    elif isinstance(service_message, HybridMessage):
        text_message = service_message.get_instruction_message()
        print(f"Service Result:\n{text_message.get_payload()}")


if __name__ == "__main__":
    main()

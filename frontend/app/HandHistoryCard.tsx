import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { SimpleActionModel } from "@/store/features/history-slice";
import convert_actions from "@/utils/action";
import convert_hole_cards from "@/utils/cards";
import convert_winnings from "@/utils/winnings";

interface Props {
    stack: number;
    setup_data: string;
    hole_cards: string[][];
    actions: SimpleActionModel[];
    winnings: number[];
    hand_id: string;
}


export const HandHistoryCard = ({setup_data, hand_id, hole_cards, winnings, actions, stack}: Props) => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Hand #{hand_id}</CardTitle>
      </CardHeader>
      <CardContent>
        <p>{`Stack: ${stack}; ${setup_data}`}</p>
        <p>{`Hands: ${convert_hole_cards(hole_cards)}`}</p>
        <p>{`Actions: ${convert_actions(actions)}`}</p>
        <p>{`Winnings: ${convert_winnings(winnings)}`}</p>
      </CardContent>
    </Card>
  );
};
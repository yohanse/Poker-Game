import { SimpleActionModel } from "@/store/features/history-slice";

export default (actions: SimpleActionModel[]) => {
    return actions.map((action, index) => {
        if (action.type === "fold" || action.type === "call") {
            return `${action.type[0]}`;
        }
        if (action.type === "check") {
            return `x`;
        }

        if (action.type === "bet" || action.type === "raise") {
            return `${action.type[0]}${action.amount}`;
        }

        if (action.type === "flop" || action.type === "turn" || action.type === "river") {
            return `${action.card}`;
        }

        if (action.type === "allin") {
            return `allin`;
        }
        return undefined
    }).filter(Boolean).join(" ");

}
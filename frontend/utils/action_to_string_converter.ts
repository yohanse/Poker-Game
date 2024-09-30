import { ActionPostItemResponse } from '../store/features/action-slice';

export default (action: ActionPostItemResponse) => {
    if (action.type === "fold" || action.type === "check" || action.type === "call") {
        return `Player ${action.player + 1} ${action.type}s`;
    }

    if (action.type === "bet") {
        return `Player ${action.player + 1} bets ${action.amount}`;
    }

    if (action.type == "allin"){
        return `Player ${action.player + 1} goes all in`;
    }

    if (action.type === "raise") {
        return `Player ${action.player + 1} raises to ${action.amount}`;
    }

    if (action.type === "flop" || action.type === "turn" || action.type === "river") {
        return `${action.type} card dealt: ${action.card}`;
    }
    return "";
};
from pokerkit import Automation, NoLimitTexasHoldem



game: NoLimitTexasHoldem = NoLimitTexasHoldem(
    (
        Automation.ANTE_POSTING,
        Automation.BET_COLLECTION,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
        Automation.HAND_KILLING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PULLING,
),
    False,
    0,
    (20, 40),
    40,
)

query = """"
SELECT 
    h.id AS hand_id,
    h.stack,
    h.setup,
    h.status,
    h.hole_cards,
    h.pot,
    h.winnings,
    h.time_stamp AS hand_time_stamp,
    json_agg(
        json_build_object(
            'id', a.id,
            'player', a.player,
            'type', a.type,
            'amount', a.amount,
            'card', a.card,
            'time_stamp', a.time_stamp
        )
    ) AS actions
FROM 
    hand h
LEFT JOIN 
    action a 
ON 
    h.id = a.hand_id
WHERE 
    h.status = false
GROUP BY 
    h.id;
"""
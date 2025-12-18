def eco_mode_decision(soc_percent):
    actions = []

    if soc_percent < 30:
        actions.append("Limit maximum acceleration")
        actions.append("Reduce HVAC power")
        actions.append("Recommend ECO driving mode")

    elif soc_percent < 50:
        actions.append("Enable ECO mode")
        actions.append("Reduce auxiliary loads")

    else:
        actions.append("Normal driving mode")

    return actions

# Example usage of the Yuqi.Protocol.JunZiNonHuman

def mock_call(input):
    if input['agent_trait'] == 'noble_like':
        return {
            "response_mode": "duty_embodied",
            "ethic_anchor": "pre-reflexive_commitment"
        }

input_data = {
    "agent_trait": "noble_like",
    "action_trigger": "external_stimulus"
}

print(mock_call(input_data))

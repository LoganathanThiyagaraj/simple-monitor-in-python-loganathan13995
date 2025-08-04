def battery_is_ok(value: float, min_val: float, max_val: float, param_name: str) -> bool:
        
    is_ok = (min_val <= value <= max_val)
    
    if not is_ok:
        print(f"{param_name} is out of range!")
        
    return is_ok

# --- Example Usage ---
if __name__ == '__main__':
    
    result = battery_is_ok(25, 0, 45, "Temperature")
    assert result is True
    
    result = battery_is_ok(50, 0, 45, "Temperature")
    assert result is False

    result = battery_is_ok(70, 20, 80, "State of Charge")
    assert result is True

    result = battery_is_ok(15, 20, 80, "State of Charge")
    assert result is False

    result = battery_is_ok(0.7, -float('inf'), 0.8, "Charge Rate")
    assert result is True

    result = battery_is_ok(0.9, -float('inf'), 0.8, "Charge Rate")
    assert result is False

    temp_ok = battery_is_ok(25, 0, 45, "Temperature")
    soc_ok = battery_is_ok(70, 20, 80, "State of Charge")
    charge_rate_ok = battery_is_ok(0.7, -float('inf'), 0.8, "Charge Rate")

    overall_ok = temp_ok and soc_ok and charge_rate_ok
    assert overall_ok is True # Example

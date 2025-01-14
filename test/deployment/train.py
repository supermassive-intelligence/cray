import masint

# masint.api_url = "https://greg1232--cray-cpu-llama-3-2-1b-instruct-fastapi-app.modal.run"
# masint.api_url = "https://greg1232--cray-nvidia-llama-3-2-3b-instruct-fastapi-app.modal.run"


def get_dataset():
    dataset = []

    count = 3

    for i in range(count):
        dataset.append(
            {"input": f"<start>{i} + {i} = ", "output": str(i + i) + "<end>"}
        )

    return dataset


llm = masint.SupermassiveIntelligence()

dataset = get_dataset()

status = llm.train(dataset, train_args={"max_steps": 100, "learning_rate": 3e-3})

print(status)

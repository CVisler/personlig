"""
if __name__ == '__main__':
    try:
        c = Construct(
                table='sst',
                period=[202321, 202322, 202323],
            )

        print(c.model_dump_json(indent=2))
        print(c.period_iso)

    except ValidationError as e:
        for i in e.errors():
            print(f'{i["msg"]} in: {i["loc"]}.\n{i["input"]} was provided.', end="\n\n")
"""

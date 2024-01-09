export function print() {
    for (let arg in arguments) {
        process.stdout.write(arg)
    }
}

export function join(array, sep) {
    return array.join(sep)
}


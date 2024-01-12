export function str(o) {
    if (o.__str) return o.__str()
    return o.toString()
}

export function substr(str, i, len) {
    return str.substr(i, len)
}

export function split(s, spliter=' ') {
    return s.split(spliter)
}

global.str = str
global.substr = substr

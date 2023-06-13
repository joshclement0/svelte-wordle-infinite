<script>

    export let letter
    export let green=''
    export let yellow=''
    export let dark=''

    $: isgreen = green.includes(letter)
    $: isyellow = isgreen ? false : yellow.includes(letter)
    $: isgrey = isgreen||isyellow ?false: dark.includes(letter)

    function firekey(){
        let event = new KeyboardEvent("keyup", {'key': letter})
        document.dispatchEvent(event)
    }
</script>

<button class="keyboard-button" class:isgreen class:isyellow class:isgrey on:submit={firekey}>{letter}</button>

<style>
.keyboard-button {
    font-size: 1rem;
    font-weight: 700;
    padding: 0.5rem;
    margin: 0 2px;
    cursor: pointer;
    text-transform: uppercase;
  }
.isgreen {
    background-color: lightgreen;
    color:black;
}
.isyellow {
    background-color: #ff9;
    color:black;
}
.isgrey {
    background-color: rgb(43, 43, 43);
    color:grey;
}
</style>
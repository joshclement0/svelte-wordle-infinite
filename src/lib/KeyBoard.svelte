<script>
    import Key from "./Key.svelte";

    export let green = ''
    export let yellow = ''
    export let dark = ''
</script>

{#key green }
<div id="keyboard-cont">
    <div class="first-row" >
        <Key bind:green bind:yellow bind:dark letter='q'/>
        <Key bind:green bind:yellow bind:dark letter='w'/>
        <Key bind:green bind:yellow bind:dark letter='e'/>
        <Key bind:green bind:yellow bind:dark letter='r'/>
        <Key bind:green bind:yellow bind:dark letter='t'/>
        <Key bind:green bind:yellow bind:dark letter='y'/>
        <Key bind:green bind:yellow bind:dark letter='u'/>
        <Key bind:green bind:yellow bind:dark letter='i'/>
        <Key bind:green bind:yellow bind:dark letter='o'/>
        <Key bind:green bind:yellow bind:dark letter='p'/>
    </div>
    <div class="second-row">
        <Key bind:green bind:yellow bind:dark letter='a'/>
        <Key bind:green bind:yellow bind:dark letter='s'/>
        <Key bind:green bind:yellow bind:dark letter='d'/>
        <Key bind:green bind:yellow bind:dark letter='f'/>
        <Key bind:green bind:yellow bind:dark letter='g'/>
        <Key bind:green bind:yellow bind:dark letter='h'/>
        <Key bind:green bind:yellow bind:dark letter='j'/>
        <Key bind:green bind:yellow bind:dark letter='k'/>
        <Key bind:green bind:yellow bind:dark letter='l'/>
    </div>
    <div class="third-row">
        <Key letter='Del'/>
        <Key bind:green bind:yellow bind:dark letter='z'/>
        <Key bind:green bind:yellow bind:dark letter='x'/>
        <Key bind:green bind:yellow bind:dark letter='c'/>
        <Key bind:green bind:yellow bind:dark letter='v'/>
        <Key bind:green bind:yellow bind:dark letter='b'/>
        <Key bind:green bind:yellow bind:dark letter='n'/>
        <Key bind:green bind:yellow bind:dark letter='m'/>
        <Key letter='Enter'/>
    </div>
</div>
{/key}
<style>
    #keyboard-cont {
        margin: 1rem 0;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #keyboard-cont div {
        display: flex;
    }

    .second-row {
        margin: 0.5rem 0;
    }

</style>
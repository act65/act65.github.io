---
layout: post
title: The Dangers of Utilitarianism
subtitle: When Doing the 'Greatest Good' Goes Wrong
---

Utilitarianism, in its simplest form, suggests that the most ethical choice is the one that will produce the greatest good for the greatest number of people. It's an appealingly simple framework. We weigh the outcomes, count the heads, and choose the path that leads to the most "utility" or happiness.

But what happens when we can't predict the future? What happens when our calculations are based on incomplete information, or when the very act of measuring "good" is fraught with peril? The classic trolley problem is often used to explore these ideas, but let's make it interactive.

### An Interactive Trolley Problem

You are standing at a lever that can switch a runaway trolley from one track to another. On the main track, there are five people tied up and unable to move. On the side track, there is one person. What do you do?

<details>
<summary>Click here to run the simulation.</summary>
<style>
    #trolley-canvas-container {
        text-align: center;
        margin: 20px auto;
    }
    #trolley-canvas {
        border: 1px solid #000;
        background: #f0f0f0;
    }
    #trolley-controls {
        margin-top: 10px;
    }
    #trolley-controls button {
        padding: 8px 16px;
        font-size: 16px;
        margin: 0 5px;
        cursor: pointer;
    }
    #trolley-outcome {
        margin-top: 10px;
        font-weight: bold;
        font-size: 18px;
        min-height: 25px;
    }
</style>

<div id="trolley-canvas-container">
    <canvas id="trolley-canvas" width="600" height="300"></canvas>
    <div id="trolley-controls">
        <button id="switch-btn">Switch Track</button>
        <button id="do-nothing-btn">Do Nothing</button>
        <button id="reset-btn">Reset</button>
    </div>
    <div id="trolley-outcome"></div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('trolley-canvas');
        const ctx = canvas.getContext('2d');
        const switchBtn = document.getElementById('switch-btn');
        const doNothingBtn = document.getElementById('do-nothing-btn');
        const resetBtn = document.getElementById('reset-btn');
        const outcomeEl = document.getElementById('trolley-outcome');
        let trolley = { x: 50, y: 150, width: 30, height: 20 };
        let animationFrameId;
        let chosenPath = null; // 'upper', 'lower', or null for initial state
        const track = {
            startY: 150,
            splitX: 200,
            curveControlX: 250,
            curveEndX: 270,
            upperY: 100,
            lowerY: 200,
            endX: 550
        };
        // Store initial state to allow for a proper reset
        const initialPeople = {
            upper: [{ x: 400, y: track.upperY }],
            lower: [
                { x: 350, y: track.lowerY },
                { x: 380, y: track.lowerY },
                { x: 410, y: track.lowerY },
                { x: 440, y: track.lowerY },
                { x: 470, y: track.lowerY }
            ]
        };
        // Create a deep copy for the active simulation state
        let people = JSON.parse(JSON.stringify(initialPeople));
        function drawTracks() {
            ctx.strokeStyle = '#666';
            ctx.lineWidth = 5;
            // Main track before split
            ctx.beginPath();
            ctx.moveTo(0, track.startY);
            ctx.lineTo(track.splitX, track.startY);
            ctx.stroke();
            // Upper track
            ctx.beginPath();
            ctx.moveTo(track.splitX, track.startY);
            ctx.quadraticCurveTo(track.curveControlX, track.startY, track.curveEndX, track.upperY);
            ctx.lineTo(track.endX, track.upperY);
            ctx.stroke();
            // Lower track
            ctx.beginPath();
            ctx.moveTo(track.splitX, track.startY);
            ctx.quadraticCurveTo(track.curveControlX, track.startY, track.curveEndX, track.lowerY);
            ctx.lineTo(track.endX, track.lowerY);
            ctx.stroke();
        }
        function drawDefaultIndicator() {
            // Only draw the indicator if no choice has been made yet
            if (chosenPath !== null) return;
            ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
            ctx.font = 'bold 16px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText('Default', track.splitX - 45, track.startY + 35);
            // Draw an arrow pointing to the lower track switch
            const arrowX = track.splitX - 15;
            const arrowY = track.startY + 15;
            ctx.beginPath();
            ctx.moveTo(arrowX, arrowY);
            ctx.lineTo(arrowX - 10, arrowY - 10);
            ctx.lineTo(arrowX - 5, arrowY - 10);
            ctx.lineTo(arrowX - 5, arrowY - 20);
            ctx.lineTo(arrowX + 5, arrowY - 20);
            ctx.lineTo(arrowX + 5, arrowY - 10);
            ctx.lineTo(arrowX + 10, arrowY - 10);
            ctx.closePath();
            ctx.fill();
        }
        function drawPerson(x, y) {
            ctx.fillStyle = 'blue';
            ctx.fillRect(x - 5, y - 20, 10, 20);
        }
        function drawTrolley() {
            ctx.fillStyle = 'red';
            ctx.fillRect(trolley.x, trolley.y - trolley.height, trolley.width, trolley.height);
        }
        function drawScene() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawTracks();
            drawDefaultIndicator();
            people.upper.forEach(p => drawPerson(p.x, p.y));
            people.lower.forEach(p => drawPerson(p.x, p.y));
            drawTrolley();
        }
        function animate() {
            trolley.x += 2;
            // Adjust Y position to follow the curve after the split
            if (trolley.x > track.splitX && trolley.x < track.curveEndX) {
                const t = (trolley.x - track.splitX) / (track.curveEndX - track.splitX);
                const startY = track.startY;
                const endY = (chosenPath === 'upper') ? track.upperY : track.lowerY;
                const controlY = track.startY;
                trolley.y = Math.pow(1 - t, 2) * startY + 2 * (1 - t) * t * controlY + Math.pow(t, 2) * endY;
            } else if (trolley.x >= track.curveEndX) {
                trolley.y = (chosenPath === 'upper') ? track.upperY : track.lowerY;
            }
            // Collision detection: remove people when the trolley's front hits them
            const trolleyFront = trolley.x + trolley.width;
            if (chosenPath === 'upper') {
                people.upper = people.upper.filter(p => p.x > trolleyFront);
            } else if (chosenPath === 'lower') {
                people.lower = people.lower.filter(p => p.x > trolleyFront);
            }
            drawScene();
            if (trolley.x > canvas.width) {
                cancelAnimationFrame(animationFrameId);
                if (chosenPath === 'upper') {
                    outcomeEl.textContent = "You switched the track. 1 person has died, 5 have been saved.";
                } else {
                    outcomeEl.textContent = "You did nothing. 5 people have died, 1 has been saved.";
                }
                return;
            }
            animationFrameId = requestAnimationFrame(animate);
        }
        function startSimulation(path) {
            if (chosenPath !== null) return; // Prevent starting if already running
            chosenPath = path;
            switchBtn.disabled = true;
            doNothingBtn.disabled = true;
            animate();
        }
        function reset() {
            cancelAnimationFrame(animationFrameId);
            trolley = { x: 50, y: 150, width: 30, height: 20 };
            chosenPath = null;
            people = JSON.parse(JSON.stringify(initialPeople)); // Deep copy from original state
            switchBtn.disabled = false;
            doNothingBtn.disabled = false;
            outcomeEl.textContent = '';
            drawScene();
        }
        switchBtn.addEventListener('click', () => startSimulation('upper'));
        doNothingBtn.addEventListener('click', () => startSimulation('lower'));
        resetBtn.addEventListener('click', reset);
        // Initial draw on page load
        reset();
    });
</script>
</details>

Most people choose to switch the track. One death is better than five. But this simple scenario assumes we have perfect knowledge. Let's explore some alternatives that reveal the fragility of our predictions.

### Twisting the Tracks: The Problem of Uncertainty

What if the situation wasn't so clear? These thought experiments, which can be adapted into the interactive example above, show how quickly the utilitarian calculus can fall apart.

*   **The Mysterious Symbol:** Imagine the same setup, but on the track with the single person, there's a large, unfamiliar symbol painted on the ground. Do you still switch the trolley?
    *   **The Twist:** After your choice, you learn the symbol means "Stop Here." By switching the trolley, you actively killed one person when doing nothing would have saved everyone. Your intervention, aimed at the greater good, caused the only fatality.

*   **The Second Trolley:** You make the seemingly obvious choice to divert the trolley, saving five people by sacrificing one.
    *   **The Twist:** A moment later, a second, unseen trolley appears from the opposite direction on the main track, killing the five people you thought you had saved. Your action cost one life and ultimately saved no one. This highlights that our choices don't exist in a vacuum; the future can hold surprises that invalidate our best-laid plans.

*   **The Unseen Consequences:** You switch the trolley, saving five and sacrificing one. A clear win for utilitarianism.
    *   **The Twist:** You later discover that the single person you sacrificed was a world-renowned surgeon on her way to perform five separate, life-saving organ transplants. Your calculation was tragically wrong because you couldn't possibly know the full "value" of each life.

### When Utilitarian Logic Leads to Devastation

These are not just abstract puzzles. History is filled with examples of utilitarian reasoning, often combined with overconfidence, leading to catastrophic outcomes.

*   **The Mutaween of Mecca:** In 2002, a fire broke out at a girls' school in Mecca. As students fled, Saudi Arabia's religious police, the Mutaween, reportedly blocked their escape and hindered rescue efforts because the girls were not wearing the proper Islamic dress (headscarves and abayas). From their perspective, the risk of the girls being seen "immodestly" was a greater harm than the risk of them dying in a fire, as it jeopardized their access to an eternal afterlife. This is a chilling example of a utilitarian calculation where the "good" being maximized is a specific religious outcome, leading to the deaths of 15 young girls.

*   **The Ford Pinto Memo:** In the 1970s, Ford Motor Company faced a decision about a known defect in the Pinto's fuel tank that made it susceptible to exploding in rear-end collisions. The company performed a cost-benefit analysis that assigned a monetary value to a human life ($200,000 at the time). They calculated that paying out damages for the predicted number of burn deaths and injuries would be cheaper than recalling and fixing every Pinto. This cold, corporate utilitarianism prioritized profit over human safety.

*   **The Bengal Famine of 1943:** During WWII, the British government under Winston Churchill enacted a "denial policy" in Bengal, India. Fearing a Japanese invasion, they seized boats and rice supplies to prevent them from falling into enemy hands. While the stated goal was the "greater good" of the war effort, this policy severely exacerbated a famine that led to the deaths of an estimated 2 to 3 million people. The needs of the empire were weighed against the lives of its subjects, with devastating results.

These examples, from the philosophical to the historical, reveal the profound dangers of a purely utilitarian approach in a world where our knowledge is incomplete and our power to predict the future is limited. The simple instruction to "do the most good" is far from simple, and acting on it can sometimes lead to the greatest harm.
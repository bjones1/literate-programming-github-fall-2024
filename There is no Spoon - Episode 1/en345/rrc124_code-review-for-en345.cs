// *RRC: I have completed the review of the following code. I found little to suggest changes on.  This reads very nicely on both VS and CCE.*<br>
// *RRC: Line spacing issues can be fixed with < b r > times however many line breaks you want.*<br>
// *RRC: My color coding is not working in CCE.  I am able to format and change the background color temporarily, but the changes do not stay.  I posted this question in Teams.*<br>
// # A program that resolves the "There is no spoon - Episode 1" problem from [Coding game website](https://www.codingame.com/home)
//
// RRC: There was an extra code block at line 2. Removed with //
//
// ## The problem and the solution
//
// <img src="There is no spoon Episode 1 solution image.png" style="width:500px;height:600px;margin:0">
//
// ## The implementation in C#
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
class Player
{
        static void Main(string[] args)
        {
          
            // ### Get Input Details
            // <br> RRC: Misspelled word on the next line fixed <br><br>
            /* _Get input details including width, height, and the lines. Use
               horizontal and vertical lines to store the input details for
               processing_ */

            int width = int.Parse(Console.ReadLine()); // the number of cells on the X axis 
            int height = int.Parse(Console.ReadLine()); // the number of cells on the Y axis 
            var lines = new List<char[]>();
            
            var verticalLines = new StringBuilder[width];
            var horizontalLines = new StringBuilder[height];

            for (int i = 0; i < height; i++)
            {
                // **width characters, each either 0 or .**
                string line = Console.ReadLine();
                lines.Add(new char[width]);
                var widthIndex = 0;
                foreach (var c in line.Trim(' ', '"'))
                {
                    lines[i][widthIndex] = c;
                    // _**If the horizontal line wasn't already added, add
                    // one**_
                    if (horizontalLines[i] == null)
                    {
                        horizontalLines[i] = new StringBuilder();
                    }

                    horizontalLines[i].Append(c);
                    // _**If the vertical line wasn't already added, add one**_
                    if (verticalLines[widthIndex] == null)
                    {
                        verticalLines[widthIndex] = new StringBuilder();
                    }
                    verticalLines[widthIndex].Append(c);
                    widthIndex++;
                }
            }
            
            var horizontalLinesStrings = horizontalLines.Select(s => s.ToString().ToCharArray().ToList()).ToArray();
            var verticalLIneStrings = verticalLines.Select(s => s.ToString().ToCharArray().ToList()).ToArray();
            
            // ### Process nodes
            //
            // \
            // RRC: There was an extra code block at line 65. Removed with //\
            // \
            // _Process nodes line by line reading each node (character) in the
            // line. If the node is not empty, find neighboring nodes (right and
            // bottom). If the node is empty ignore it._\
            // \
            // RRC: There was an extra code block at line 69. Removed with //\
            // \
            // _Since the approach to find the next node uses C# List IndexOf
            // method, keep track of the nodes found and don't use the node
            // again for each line._
            var processedNodes = new Dictionary<string, string>();
            for (var i = 0; i < lines.Count(); i++)
            {
                var horizontalLine = horizontalLinesStrings[i];
                
                processedNodes.Clear();
                for (var j = 0; j < width; j++)
                {
                    var verticalLine = verticalLIneStrings[j];

                    if (horizontalLine[j] == '.')
                    {
                        // **_Ignore nodes with ._**
                        continue; 
                    }
                    // **Next node in the line**
                    var node = $"{j} {i}";
                    
                    // **Next node to the right**
                    var nextNodeToRight = $"-1 -1";
                    if (j + 1 < width)
                    {
                        var nextIndex = horizontalLine.IndexOf('0', j + 1);
                        var node1 = $"{nextIndex} {i}";
                        
                        if (nextIndex >= 0)
                        {
                            nextNodeToRight = node1;
                            processedNodes.Add(node1, "");
                        }
                    }

                    // **Next node to the bottom**
                    var nextNodeToBottom = "-1 -1";
                    if (i + 1 < lines.Count())
                    {
                        var nextIndex = verticalLine.IndexOf('0', i + 1);
                        var node2 = $"{j} {nextIndex}";
                        
                        if (nextIndex >= 0)
                        {
                            nextNodeToBottom = node2;
                            processedNodes.Add(node2, "");
                        }
                    }
                    // _If no neighboring node found -1 -1 will be used as the
                    // coordinate_
                    //
                    // \_\_
                    //
                    // _Output the node and neighboring nodes coordinates_
                    //
                    // \_\_
                    Console.WriteLine($"{node} {nextNodeToRight} {nextNodeToBottom}");
                }
            }
        }
    }